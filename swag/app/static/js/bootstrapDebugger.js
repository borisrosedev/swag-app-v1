


function bodyDefaultPropertiesSetter(){
    console.log("✅ [body-default-properties-setter] activated")
    const body = document.getElementsByTagName("body")[0];
    body.style.removeProperty("overflow")
    body.style.removeProperty("padding-right")
}

bodyDefaultPropertiesSetter()
