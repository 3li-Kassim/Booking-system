window.onload = () =>{


const dropdown = document.getElementById("service");
function getSelectedOption(){
    const value = dropdown.value;
    return value;
}

if(dropdown !== null){
    
dropdown.addEventListener("change",()=>{
const other = document.getElementById("other");
const labelOther = document.getElementById("label-other")
if(getSelectedOption() === "other"){
    
    other.style.display = "block";
    labelOther.style.display = "block";
}
else{
    other.style.display = "none";
    labelOther.style.display = "none";
}
})
}

setTimeout(() =>{
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(f => f.style.display = 'none');
},3000);





}