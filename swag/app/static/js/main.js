import { initGsapAnimations } from "./initGsap.js";
import { initPurchaseChart } from "./initCharts.js";
import { bodyDefaultPropertiesSetter } from "./bootstrapDebugger.js"


function handleHtmxAfterSwap(event) {
    if (event.detail.target.id === 'root') {
        bodyDefaultPropertiesSetter()
        if (document.querySelector('#dashboard-main')) {
            initPurchaseChart();
        }

        if(document.querySelector('#signup-main')){
            function previewPhoto(event) {
                const file = event.target.files[0];
                const preview = document.getElementById("preview");
                if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    preview.innerHTML = `<img src="${e.target.result}" style="max-width:200px">`;
                };
                reader.readAsDataURL(file);
                }
            }
        }

        initGsapAnimations();
        
    }
}

document.addEventListener('DOMContentLoaded', () => {
   
    document.body.addEventListener('htmx:afterSwap', handleHtmxAfterSwap);
    initGsapAnimations();
});