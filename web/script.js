console.log("Welcome to Emotion Recognizer!");

async function show_happy_emotion(){
    var emotion_data = await eel.get_data()();
    const count = Object.keys(emotion_data).length;
    console.log("working!"+count);

    for (let i = 0; i < count; i++) {
        var id = "img-" + i.toString();
        // console.log(emotion_data[id]);
        document.getElementById(id).src = emotion_data[id];
    }
}
// show_happy_emotion();

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
        show_happy_emotion();
    } else {
        displayEmotion.innerText = "You looks " + emotion + "!";
    }

});
