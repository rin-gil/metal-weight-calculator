"""Fills the databases with values at the first start of the application"""

from metal_calc.models import MetalAlloy, Metal, MetalShape, PageInfo


def fill_pageinfo_table() -> None:
    """Fills the database in the PageInfo model"""
    page_info_data_en: dict = {
        "title": "Metal weight calculator",
        "description": "Metal weight calculator - a program designed to calculate the weight of pipes, channels, rebar, beams and other rolled metal.",
        "keywords": "metal weight calculator, metal calculator, metal calculator online, metal calculator online, metal calculator, metal weight calculation",
    }
    page_info_data_ru: dict = {
        "title": "Калькулятор веса металла",
        "description": "Калькулятор веса металла - программа, предназначенная для расчета веса труб, швеллеров, арматуры, балок и прочего металлопроката.",
        "keywords": "калькулятор веса металла, металлический калькулятор, калькулятор металла онлайн, металлокалькулятор онлайн, металл калькулятор, расчет веса металла",
    }
    page_info_data_uk: dict = {
        "title": "Калькулятор ваги металу",
        "description": "Калькулятор ваги металу - програма, призначена для розрахунку ваги труб, швелерів, арматури, балок та іншого металопрокату.",
        "keywords": "калькулятор ваги металу, металевий калькулятор, калькулятор металу онлайн, металокалькулятор онлайн, метал калькулятор, розрахунок ваги металу",
    }
    pageinfo: PageInfo = PageInfo.objects.create(
        title=page_info_data_en.get("title"),
        title_en=page_info_data_en.get("title"),
        title_ru=page_info_data_ru.get("title"),
        title_uk=page_info_data_uk.get("title"),
        description=page_info_data_en.get("description"),
        description_en=page_info_data_en.get("description"),
        description_ru=page_info_data_ru.get("description"),
        description_uk=page_info_data_uk.get("description"),
        keywords=page_info_data_en.get("keywords"),
        keywords_en=page_info_data_en.get("keywords"),
        keywords_ru=page_info_data_ru.get("keywords"),
        keywords_uk=page_info_data_uk.get("keywords"),
    )
    pageinfo.save()


def fill_metalshape_table() -> None:
    """Fills the database in the MetalShape model"""
    metal_shapes_data: dict[int, tuple] = {
        1: ("Beam", "Балка", "Балка"),
        2: ("Square bar", "Квадрат", "Квадрат"),
        3: ("Round bar", "Круг", "Круг"),
        4: ("Sheet", "Лист", "Лист"),
        5: ("Flat bar", "Полоса", "Смуга"),
        6: ("Round tube", "Труба", "Труба"),
        7: ("Profile tube", "Труба профильная", "Труба профільна"),
        8: ("Metal angle", "Уголок", "Кутник"),
        9: ("Metal channel", "Швеллер", "Швелер"),
        10: ("Hex bar", "Шестигранник", "Шестигранник"),
    }
    metal_shapes: list[MetalShape] = []
    for key, value in metal_shapes_data.items():
        metal_shapes.append(
            MetalShape(
                id=key, shape_name=value[0], shape_name_en=value[0], shape_name_ru=value[1], shape_name_uk=value[2]
            )
        )
    MetalShape.objects.bulk_create(metal_shapes)


def fill_metal_table() -> None:
    """Fills the database in the Metal model"""
    metals_data: dict[int, tuple] = {
        1: ("Steel", "Сталь", "Сталь", 7800),
        2: ("Cast iron", "Чугун", "Чавун", 7500),
        3: ("Aluminum", "Алюминий", "Алюміній", 2690),
        4: ("Bronze", "Бронза", "Бронза", 8000),
        5: ("Brass", "Латунь", "Латунь", 8500),
        6: ("Copper", "Медь", "Мідь", 8960),
        7: ("Titan", "Титан", "Титан", 4500),
    }
    metals: list = []
    for key, value in metals_data.items():
        metals.append(
            Metal(
                id=key,
                metal_name=value[0],
                metal_name_en=value[0],
                metal_name_ru=value[1],
                metal_name_uk=value[2],
                density=value[3],
            )
        )
    Metal.objects.bulk_create(metals)


def fill_metalalloy_table() -> None:
    """Fills the database in the MetalAlloy model"""
    metal_alloys_data: dict[int, tuple] = {
        1: (  # Steel
            ("08H13", "08Х13", 7760),
            ("08H17T", "08Х17Т", 7760),
            ("08H18N10", "08Х18Н10", 7850),
            ("08H18N10T", "08Х18Н10Т", 7900),
            ("09G2S", "09Г2С", 7850),
            ("10", "10", 7850),
            ("10H17N13M2T", "10Х17Н13М2Т", 7900),
            ("10H17N13M3T", "10Х17Н13М3Т", 7900),
            ("10HSND", "10ХСНД", 7850),
            ("110G13L", "110Г13Л", 7820),
            ("12H13", "12Х13", 7720),
            ("12H18N10T", "12Х18Н10Т", 7900),
            ("12H1MF", "12Х1МФ", 7800),
            ("14H17N2", "14Х17Н2", 7750),
            ("15H25T", "15Х25Т", 7700),
            ("15H5M", "15Х5М", 7750),
            ("15HSND", "15ХСНД", 7850),
            ("20", "20", 7850),
            ("20L", "20Л", 7850),
            ("20H13", "20Х13", 7670),
            ("20H23N18", "20Х23Н18", 7900),
            ("30H", "30Х", 7820),
            ("30H13", "30Х13", 7670),
            ("38HN3MA", "38ХН3МА", 7850),
            ("40H", "40Х", 7820),
            ("40H13", "40Х13", 7650),
            ("45", "45", 7820),
            ("5HNM", "5ХНМ", 7800),
            ("60G", "60Г", 7810),
            ("60S2A", "60С2А", 7680),
            ("65", "65", 7810),
            ("65G", "65Г", 7850),
            ("70", "70", 7810),
            ("95H18", "95Х18", 7750),
            ("AISI 304", "AISI 304", 7850),
            ("AISI 304L", "AISI 304L", 7850),
            ("AISI 316L", "AISI 316L", 8000),
            ("AISI 316Ti", "AISI 316Ti", 7950),
            ("AISI 321", "AISI 321", 7900),
            ("AISI 409", "AISI 409", 7760),
            ("AISI 410", "AISI 410", 7720),
            ("AISI 420", "AISI 420", 7650),
            ("AISI 420S", "AISI 420S", 7670),
            ("AISI 430", "AISI 430", 7720),
            ("AISI 439", "AISI 439", 7700),
            ("AISI 904L", "AISI 904L", 7960),
            ("R6M5", "Р6М5", 8300),
            ("St1", "Ст1", 7850),
            ("St3kp", "Ст3кп", 7800),
            ("St3ps", "Ст3пс", 7800),
            ("St3sp", "Ст3сп", 7870),
            ("U10", "У10", 7810),
            ("U10A", "У10А", 7810),
            ("U12A", "У12А", 7810),
            ("U7", "У7", 7830),
            ("U8", "У8", 7839),
            ("U8A", "У8А", 7830),
            ("H15N60", "Х15Н60", 8500),
            ("H20N80", "Х20Н80", 8400),
            ("H23Ju5T", "Х23Ю5Т", 7210),
            ("ShH15", "ШХ15", 7810),
            ("ShH4", "ШХ4", 7850),
        ),
        2: (  # Cast iron
            ("SCh10", "СЧ10", 6800),
            ("SCh15", "СЧ15", 7000),
            ("SCh20", "СЧ20", 7100),
            ("SCh25", "СЧ25", 7200),
            ("SCh35", "СЧ35", 7400),
        ),
        3: (
            ("1420", "1420", 2470),
            ("A5", "А5", 2710),
            ("A85", "А85", 2700),
            ("A95", "А95", 2710),
            ("A97", "А97", 2710),
            ("A99", "А99", 2700),
            ("A999", "А999", 2710),
            ("AV", "АВ", 2700),
            ("AD", "АД", 2710),
            ("AD0", "АД0", 2710),
            ("AD1", "АД1", 2710),
            ("AD31", "АД31", 2710),
            ("AD33", "АД33", 2710),
            ("AK4", "АК4", 2770),
            ("AK4-1", "АК4-1", 2800),
            ("AK5M7", "АК5М7", 2850),
            ("AK6", "АК6", 2750),
            ("AK8", "АК8", 2800),
            ("AL1", "АЛ1", 2750),
            ("AL19", "АЛ19", 2780),
            ("AL2", "АЛ2", 2650),
            ("AL3", "АЛ3", 2700),
            ("AL32", "АЛ32", 2650),
            ("AL4", "АЛ4", 2650),
            ("AL5", "АЛ5", 2680),
            ("AL7", "АЛ7", 2800),
            ("AL8", "АЛ8", 2550),
            ("AL9", "АЛ9", 2660),
            ("AMg1", "АМг1", 2670),
            ("AMg2", "АМг2", 2680),
            ("AMg3", "АМг3", 2670),
            ("AMg5", "АМг5", 2650),
            ("AMg5P", "АМг5П", 2650),
            ("AMg6", "АМг6", 2640),
            ("AMts", "АМц", 2730),
            ("AN-2.5", "АН-2.5", 2800),
            ("V65", "В65", 2800),
            ("V93", "В93", 2840),
            ("V94", "В94", 2850),
            ("V95", "В95", 2850),
            ("VAL10", "ВАЛ10", 2800),
            ("D1", "Д1", 2800),
            ("D16", "Д16", 2800),
            ("D18", "Д18", 2760),
            ("D19", "Д19", 2760),
        ),  # Aluminum
        4: (  # Bronze
            ("BrA5", "БрА5", 8200),
            ("BrA7", "БрА7", 7800),
            ("BrA9Zh3L", "БрА9Ж3Л", 7600),
            ("BrA9Zh4", "БрА9Ж4", 7600),
            ("BrAZh9-4", "БрАЖ9-4", 7600),
            ("BrAZhN10-4-4", "БрАЖН10-4-4", 7500),
            ("BrAMts9-2", "БрАМц9-2", 7600),
            ("BrB2", "БрБ2", 8200),
            ("BrB2.5", "БрБ2.5", 8230),
            ("BrKMts3-1", "БрКМц3-1", 8400),
            ("BrKN1-3", "БрКН1-3", 8800),
            ("BrO10", "БрО10", 8800),
            ("BrO10F1", "БрО10Ф1", 8760),
            ("BrO10Ts2", "БрО10Ц2", 8500),
            ("BrO5Ts5S5", "БрО5Ц5С5", 8800),
            ("BrO8S12", "БрО8С12", 9100),
            ("BrOF6.5-0.15", "БрОФ6.5-0.15", 8800),
            ("BrOTs4-3", "БрОЦ4-3", 8800),
            ("BrOTsS4-4-2.5", "БрОЦС4-4-2.5", 8900),
            ("BrOTsS4-4-4", "БрОЦС4-4-4", 9100),
            ("BrS30", "БрС30", 9540),
            ("BrH1", "БрХ1", 8900),
        ),
        5: (  # Brass
            ("L59", "Л59", 8400),
            ("L60", "Л60", 8400),
            ("L63", "Л63", 8440),
            ("L66", "Л66", 8470),
            ("L68", "Л68", 8600),
            ("L70", "Л70", 8610),
            ("L75", "Л75", 8630),
            ("L80", "Л80", 8660),
            ("L85", "Л85", 8750),
            ("L90", "Л90", 8780),
            ("L96", "Л96", 8850),
            ("LA77-2", "ЛА77-2", 8600),
            ("LAZh60-1-1", "ЛАЖ60-1-1", 8200),
            ("LZhMts59-1-1", "ЛЖМц59-1-1", 8500),
            ("LZhS58-1-1", "ЛЖС58-1-1", 8400),
            ("LK80-3", "ЛК80-3", 8200),
            ("LMts58-2", "ЛМц58-2", 8400),
            ("LO60-1", "ЛО60-1", 8500),
            ("LO62-1", "ЛО62-1", 8500),
            ("LO70-1", "ЛО70-1", 8600),
            ("LS59-1", "ЛС59-1", 8450),
            ("LS63-3", "ЛС63-3", 8500),
            ("LS64-2", "ЛС64-2", 8500),
            ("LTs16K4", "ЛЦ16К4", 8300),
            ("LTs23A6Zh3Mts2", "ЛЦ23А6Ж3Мц2", 8500),
            ("LTs30A3", "ЛЦ30А3", 8500),
            ("LTs38Mts2S2", "ЛЦ38Мц2С2", 8500),
            ("LTs40S", "ЛЦ40С", 8500),
        ),
        6: (  # Copper
            ("BrKd1", "БрКд1", 8940),
            ("BrNBT", "БрНБТ", 8830),
            ("BrNHK", "БрНХК", 8850),
            ("BrH", "БрХ", 8920),
            ("BrHTsr", "БрХЦр", 8900),
            ("M0", "М0", 8940),
            ("M00", "М00", 8940),
            ("M00b", "М00б", 8940),
            ("M0b", "М0б", 8940),
            ("M0k", "М0к", 8940),
            ("M1", "М1", 8930),
            ("M1k", "М1к", 8940),
            ("M1r", "М1р", 8940),
            ("M1f", "М1ф", 8940),
            ("M2", "М2", 8940),
            ("M3", "М3", 8940),
            ("M3r", "М3р", 8940),
            ("MK", "МК", 8920),
            ("MN19", "МН19", 8900),
            ("MNZh5-1", "МНЖ5-1", 8700),
            ("MNMts3-12", "МНМц3-12", 8400),
            ("MNMts40-1.5", "МНМц40-1.5", 8900),
            ("MNMts43-0.5", "МНМц43-0.5", 8900),
            ("MNTs15-20", "МНЦ15-20", 8700),
            ("NMZhMts28-2.5-1.5", "НМЖМц28-2.5-1.5", 7800),
        ),
        7: (  # Titan
            ("VT1-0", "ВТ1-0", 4505),
            ("VT1-00", "ВТ1-00", 4505),
            ("VT1-1", "ВТ1-1", 4505),
            ("VT14", "ВТ14", 4520),
            ("VT20", "ВТ20", 4450),
            ("VT22", "ВТ22", 4600),
            ("VT3-1", "ВТ3-1", 4500),
            ("VT5", "ВТ5", 4400),
            ("VT5-1", "ВТ5-1", 4460),
            ("VT6", "ВТ6", 4430),
            ("OT4-1", "ОТ4-1", 4550),
            ("PT7M", "ПТ7М", 4490),
        ),
    }
    metal_alloys: list = []
    for key, values in metal_alloys_data.items():
        for value in values:
            metal_alloys.append(
                MetalAlloy(
                    metal_id=key,
                    metal_alloy=value[0],
                    metal_alloy_en=value[0],
                    metal_alloy_ru=value[1],
                    metal_alloy_uk=value[1],
                    density=value[2],
                )
            )
    MetalAlloy.objects.bulk_create(metal_alloys)


def fill_db() -> None:
    """Fills the databases with initial values"""
    if not PageInfo.objects.all():
        PageInfo.objects.all().delete()
        fill_pageinfo_table()
    if not MetalShape.objects.all():
        MetalShape.objects.all().delete()
        fill_metalshape_table()
    if not Metal.objects.all():
        Metal.objects.all().delete()
        fill_metal_table()
    if not MetalAlloy.objects.all():
        MetalAlloy.objects.all().delete()
        fill_metalalloy_table()
