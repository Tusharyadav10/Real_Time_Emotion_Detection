console.log("Welcome to Emotion Recognizer!");

async function show_motivational_media() {
    var emotion_data = await eel.get_data()();
    const count = Object.keys(emotion_data).length;
    console.log("working!" + count);
    // console.log(emotion_data["img-0"]);
    // console.log(emotion_data["img-0"][0]);
    // console.log(emotion_data["img-0"][1]);

    for (let i = 0; i < count; i++) {
        var id = "img-" + i.toString();
        if (emotion_data[id][0] == "Motivation") {
            document.getElementById("img-" + (count - i - 1).toString()).src = emotion_data[id][1];
        }
    }
}
// show_motivational_media();

async function show_happy_media() {
    var emotion_data = await eel.get_data()();
    const count = Object.keys(emotion_data).length;
    console.log("working!" + count);

    for (let i = 0; i < count; i++) {
        var id = "img-" + i.toString();
        // console.log(emotion_data[id]);
        if (emotion_data[id][0] == "Happy") {
            document.getElementById(id).src = emotion_data[id][1];
        }
    }
}
// show_happy_media();

function updateEmotion(emotion, percentage) {
    document.getElementById("currentEmotion").textContent = emotion;
    document.getElementById("emotionPercentageBar").style.width = percentage + "%";
    document.getElementById("emotionPercentageText").textContent = percentage + "%";
}

function updateBarHeights(emotionData) {
    for (const [emotion, percentage] of Object.entries(emotionData)) {
        const bar = document.getElementById(emotion.toLowerCase() + 'Bar');
        if (bar) {
            bar.style.height = parseInt(percentage) + 'px';
        }
    }
}


const landingPage = document.getElementById("landing-page");
const dashboard = document.getElementById("dashboard");
const recommendBox = document.getElementById("recommend-box");
const startBtn = document.getElementById("start-btn");
const changeMoodBtn = document.getElementById("changeMoodBtn");
const displayEmotion = document.getElementById("display-emotion");
var curr_emotion = 'Happy';

startBtn.addEventListener("click", async () => {
    startBtn.disabled = true;
    var timeSelect = document.getElementById("timeSelect").value;
    // console.log(timeSelect);
    var emotionLst = await eel.detect_emotion(timeSelect)();
    // console.log(emotionLst);
    landingPage.hidden = true;
    dashboard.hidden = false;

    updateBarHeights(emotionLst);

    var curr_perc = 0;
    for (const [emotion, percentage] of Object.entries(emotionLst)) {
        if (curr_perc < parseInt(percentage)) {
            curr_emotion = emotion;
            curr_perc = parseInt(percentage);
        }
    }
    updateEmotion(curr_emotion, curr_perc);
});

changeMoodBtn.addEventListener("click", () => {
    if (curr_emotion == "Sad") {
        dashboard.hidden = true;
        recommendBox.hidden = false;
        show_motivational_media();
    }
    else if (curr_emotion == "Angry") {
        dashboard.hidden = true;
        recommendBox.hidden = false;
        show_happy_media();
    }
    else {
        alert("You are" + curr_emotion + ". No need to change mood");
    }
    
});