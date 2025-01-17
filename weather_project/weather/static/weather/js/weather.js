document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.querySelector('.temperature');
    const feelsLikeElement = document.querySelector('.feels-like');
    const tempMaxElement = document.querySelector('.temp-max');
    const tempMinElement = document.querySelector('.temp-min');
    const unitButtons = document.querySelectorAll('[data-unit]');

    function kelvinToCelsius(kelvin) {
        return kelvin - 273.15;
    }

    function kelvinToFahrenheit(kelvin) {
        return (kelvin - 273.15) * 9/5 + 32;
    }

    function updateTemperature(element, kelvin, unit) {
        let temperature;
        switch(unit) {
            case 'C':
                temperature = kelvinToCelsius(kelvin);
                break;
            case 'F':
                temperature = kelvinToFahrenheit(kelvin);
                break;
            default:
                temperature = kelvin;
        }
        element.textContent = `${temperature.toFixed(2)}°${unit}`;
    }

    function updateAllTemperatures(unit) {
        const elements = [
            { el: temperatureElement, kelvin: parseFloat(temperatureElement.dataset.kelvin) },
            { el: feelsLikeElement, kelvin: parseFloat(feelsLikeElement.dataset.kelvin) },
            { el: tempMaxElement, kelvin: parseFloat(tempMaxElement.dataset.kelvin) },
            { el: tempMinElement, kelvin: parseFloat(tempMinElement.dataset.kelvin) }
        ];

        elements.forEach(item => updateTemperature(item.el, item.kelvin, unit));
    }

    unitButtons.forEach(button => {
        button.addEventListener('click', function() {
            const unit = this.dataset.unit;
            updateAllTemperatures(unit);
            unitButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Initialize with Celsius
    updateAllTemperatures('C');
});

