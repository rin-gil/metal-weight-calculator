/**
 * When selecting a metal type, switches the visibility of the items in the list of alloys, according to the selected metal type.
 *
 * @return void
 * @param selectedMetal selected type of metal
 */
function selectMetal(selectedMetal) {
    let i, options;
    options = document.getElementsByClassName('grade');
    for (i = 0; i < options.length; i++) {
        if (options[i].className.includes(selectedMetal)) {
            options[i].className = options[i].className.replace('hidden', 'visible')
        } else {
            options[i].className = options[i].className.replace('visible', 'hidden')
            options[i].removeAttribute('selected')
        }
    }
    document.getElementById('metal_alloy').value = 0
    // When selecting a metal, it also changes the value sent to the form with id="calculator"
    document.getElementById('metal_alloy_selected').value = 0
    document.getElementById('metal_selected').value = selectedMetal
}

/**
 * When selecting a metal alloy, it also changes the value sent to the form with id="calculator"
 *
 * @return void
 * @param selectedAlloy selected alloy of metal
 */
function selectMetalAlloy(selectedAlloy) {
    document.getElementById('metal_alloy_selected').value = selectedAlloy
}


/**
 * Allows only numbers to be entered in the input boxes.
 */
function enterNumbersOnly() {
    if (event.keyCode < 48 || event.keyCode > 57)
        event.returnValue = false;
}