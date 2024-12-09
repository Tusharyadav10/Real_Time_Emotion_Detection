console.log("Welcome to Emotion Recognizer!");

async function show_motivational_media(){
    var emotion_data = await eel.get_data()();
    const count = Object.keys(emotion_data).length;
    console.log("working!"+count);
    // console.log(emotion_data["img-0"]);
    // console.log(emotion_data["img-0"][0]);
    // console.log(emotion_data["img-0"][1]);

    for (let i = 0; i < count; i++) {
        var id = "img-" + i.toString();
        if(emotion_data[id][0] == "Motivation"){
            document.getElementById("img-" + (count-i-1).toString()).src = emotion_data[id][1];
        }     
    }
}
// show_motivational_media();

async function show_happy_media(){
    var emotion_data = await eel.get_data()();
    const count = Object.keys(emotion_data).length;
    console.log("working!"+count);

    for (let i = 0; i < count; i++) {
        var id = "img-" + i.toString();
        // console.log(emotion_data[id]);
        if(emotion_data[id][0] == "Happy"){
            document.getElementById(id).src = emotion_data[id][1];
        } 
    }
}
// show_happy_media();

const landingPage = document.getElementById("landing-page");
const recommendBox = document.getElementById("recommend-box");
const startBtn = document.getElementById("start-btn");
const displayEmotion = document.getElementById("display-emotion");

startBtn.addEventListener("click", async () => {
    var emotion = await eel.detect_emotion()();
    console.log(emotion);
    if(emotion == "Sad") {
        landingPage.hidden = true;
        recommendBox.hidden = false;
        show_motivational_media();
    }
    else if(emotion == "Angry") {
        landingPage.hidden = true;
        recommendBox.hidden = false;
        show_happy_media();
    } 
    else {
        displayEmotion.innerText = "You looks " + emotion + "!";
    }

});
