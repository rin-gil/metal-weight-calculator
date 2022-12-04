"""Provides a metal calculator"""

from typing import TypedDict

from django.http import QueryDict

from metal_calc.models import MetalGrade, Metals, MetalShape


class ContextData(TypedDict):
    """Describes values for fields in the calculator"""
    shape_selected: int
    metal_type_selected: int
    metal_alloy_selected: int
    error_message: bool
    width: int
    height: int
    s: int
    s2: int
    diameter: int
    quantity: int
    length: int
    weight: str


default_context_data: ContextData = {
    "shape_selected": 1,
    "metal_type_selected": 1,
    "metal_alloy_selected": 0,
    "error_message": False,
    "width": 0,
    "height": 0,
    "s": 0,
    "s2": 0,
    "diameter": 0,
    "quantity": 0,
    "length": 0,
    "weight": "0.00",
}


def _parse_shape(shape: str | None) -> int:
    """Checks the correctness of the selected metal shape"""
    if shape in tuple(map(str, MetalShape.objects.values_list("id", flat=True))):
        return int(shape)
    return default_context_data["shape_selected"]


def _parse_metal_type(metal_type: str | None) -> int:
    """Checks the correctness of the selected metal type"""
    if metal_type in tuple(map(str, Metals.objects.values_list("id", flat=True))):
        return int(metal_type)
    return default_context_data["metal_type_selected"]


def _parse_metal_alloy(metal_alloy: str | None) -> int:
    """Checks the correctness of the selected metal alloy"""
    if metal_alloy in tuple(map(str, MetalGrade.objects.values_list("id", flat=True))):
        return int(metal_alloy)
    return default_context_data["metal_alloy_selected"]


def _parse_value(checked_value: str | None) -> int:
    """Checks if the values entered by the user are correct"""
    if not checked_value:
        return 0
    try:
        return int(checked_value)
    except (TypeError, ValueError):
        return 0


def _calculate_weight_of_metal(volume: float, metal_type_selected: int, metal_alloy_selected: int) -> str:
    """Calculates the weight of the metal from the data entered by the user"""
    if metal_alloy_selected == 0:
        density: int = Metals.objects.get(pk=metal_type_selected).density
    else:
        density = MetalGrade.objects.get(pk=metal_alloy_selected).density
    return f"{round(volume * density, 2):.2f}"


def get_context_data_for_calculator_fields(request: QueryDict, context: ContextData) -> ContextData:
    """
    Sets the values of the calculator fields based on the data entered by the user.

    :param request: POST request received from a form on the site
    :param context: dictionary with initial fields for the form on the site
    :return: dictionary with new values of fields, which will be displayed in the form on the site
    """

    shape_selected: int = _parse_shape(shape=request.get("metal_shape"))
    metal_type_selected: int = _parse_metal_type(metal_type=request.get("metal_type"))
    metal_alloy_selected: int = _parse_metal_alloy(metal_alloy=request.get("metal_alloy"))

    width: int = _parse_value(checked_value=request.get("width"))
    height: int = _parse_value(checked_value=request.get("height"))
    s: int = _parse_value(checked_value=request.get("s"))
    s2: int = _parse_value(checked_value=request.get("s2"))
    diameter: int = _parse_value(checked_value=request.get("diameter"))
    quantity: int = _parse_value(checked_value=request.get("quantity"))
    length: int = _parse_value(checked_value=request.get("length"))

    if shape_selected == 1:
        if width < s2 or height < (s * 2):
            volume: float = 0.0
            context["error_message"] = True
        else:
            volume = (((width * height) - 2 * ((height - 2 * s) * ((width - s2) / 2))) / 1000000) * length
    elif shape_selected == 2:
        volume = ((width ** 2) / 1000000) * length
    elif shape_selected == 3:
        volume = (3.141592653589793 * diameter ** 2 / 4 / 1000000) * length
    elif shape_selected == 4:
        volume = (width * height / 1000000) * s * quantity / 1000
    elif shape_selected == 5:
        volume = (width * length / 1000) * s / 1000
    elif shape_selected == 6:
        if diameter < s * 2:
            volume = 0.0
            context["error_message"] = True
        else:
            volume = (3.141592653589793 * (diameter ** 2 - (diameter - s * 2) ** 2) / 4 / 1000000) * length
    elif shape_selected == 7:
        if min(width, height) < s * 2:
            volume = 0.0
            context["error_message"] = True
        else:
            volume = (width * height - (width - s * 2) * (height - s * 2)) / 1000000 * length
    elif shape_selected == 8:
        if min(width, height) < s:
            volume = 0.0
            context["error_message"] = True
        else:
            volume = (((width * s) + ((height - s) * s)) / 1000000) * length
    elif shape_selected == 9:
        if width < s * 2 or height < s:
            volume = 0.0
            context["error_message"] = True
        else:
            volume = (((width * s) + ((height - s) * s * 2)) / 1000000) * length
    elif shape_selected == 10:
        volume = (2 * (3 ** 0.5) * ((diameter / 1000) / 2) ** 2) * length
    else:
        volume = 0.0

    weight: str = _calculate_weight_of_metal(
        volume=volume, metal_type_selected=metal_type_selected, metal_alloy_selected=metal_alloy_selected
    )

    context["shape_selected"] = shape_selected
    context["metal_type_selected"] = metal_type_selected
    context["metal_alloy_selected"] = metal_alloy_selected
    context["width"] = width
    context["height"] = height
    context["s"] = s
    context["s2"] = s2
    context["diameter"] = diameter
    context["quantity"] = quantity
    context["length"] = length
    context["weight"] = weight

    return context
