window.addEventListener("load", () => {
  const playlist = document.getElementById("playlist");
  const audioPlayer = document.getElementById("audio-player");

  playlist.addEventListener("click", (event) => {
    const clickedSong = event.target;
    const songSource = clickedSong.getAttribute("data-src");

    if (songSource) {
      audioPlayer.src = songSource;
      audioPlayer.play();
    }
  });
});

let tabsBtn = document.querySelectorAll("#tabsBtn");
let tabsItems = document.querySelectorAll(".audio__first");
tabsBtn.forEach((item) => {
  item.addEventListener("click", () => {
    let currentBtn = item;
    let tabId = currentBtn.getAttribute("data-tab");
    let currentTab = document.querySelector(tabId);
    if (!currentBtn.classList.contains("active")) {
      tabsBtn.forEach((item) => {
        item.classList.remove("active");
      });
      tabsItems.forEach((item) => {
        item.classList.remove("active");
      });
      currentBtn.classList.add("active");
      currentTab.classList.add("active");
    }
  });
});
document.querySelector("#tabsBtn").click();
