let hold_breath_progress;
let hold_out_progress;
let hold_in_progress;
let text_breath_num;
let text_breath_title;

$(document).ready(function () {

    let mode = 0;
    let second_num = 5000;
    let breath_in = 3000;
    let breath_out = 5000;
    let hold_in = 2000;
    let hold_out = 2000;

    let breathInterval;
    let updateProgressUIInterval;

    // for breath
    initBreath();

    const breath = function breath() {
        if (second_num % 1000 == 0 && second_num != 0) {
            $(".text_breath_num").addClass("animated_second_text")
            text_breath_num.innerHTML = "0" + second_num / 1000;
        } else {
            $(".text_breath_num").removeClass("animated_second_text")
        }
        second_num = second_num - 100;

        if ((mode == 0 || mode == 3) && second_num == -100) {

            if (hold_out == 0) {
                second_num = breath_in;
                mode = 1;
                text_breath_title.innerHTML = "Hít vào"

            } else {
                second_num = hold_out;
                mode = 4;
                text_breath_title.innerHTML = "Giữ hơi thở"
            }
        }

        if (mode == 4 && second_num == -100) {
            second_num = breath_in;
            mode = 1;
            text_breath_title.innerHTML = "Hít vào"
        }

        if (mode == 1 && second_num == -100) {

            if (hold_in == 0) {
                second_num = breath_out;
                mode = 3;
                text_breath_title.innerHTML = "Thở ra"
            } else {
                second_num = hold_in;
                mode = 2;
                text_breath_title.innerHTML = "Giữ hơi thở"
            }
        }

        if (mode == 2 && second_num == -100) {
            second_num = breath_out;
            mode = 3;
            text_breath_title.innerHTML = "Thở ra"
        }
    };
    const updateProgressUI = function updateProgressUI() {
        if (mode == 1) {
            let hold_breath_value = second_num * 100 / breath_in;
            hold_breath_progress.css('width', hold_breath_value + '%').attr('aria-valuenow', hold_breath_value);
        }

        if (mode == 3) {
            let hold_breath_value = (breath_out - second_num) * 100 / breath_out;
            hold_breath_progress.css('width', hold_breath_value + '%').attr('aria-valuenow', hold_breath_value);
        }
    }

    initTitle();

    initSocial();

    initMusicList(breathInterval, updateProgressUIInterval, breath, updateProgressUI);

    initSoundList();

    initTheme();

});


function initTitle() {
    var title = document.title + " " + "|" + " ";
    setInterval(function () {
        title = title.substring(1) + title.charAt(0);
        document.title = title;
    }, 400);
}

function initSocial() {
    // social link
    const FACEBOOK_URL = 'https://www.facebook.com/Thi%E1%BB%81n-%C4%90%E1%BB%8Bnh-Online-107349881540626';
    const YOUTUBE_CHANNEL = 'https://www.youtube.com/channel/UCj5L3C0oWn9WQ8IWfvKV-Dg?sub_confirmation=1'

    const social_facebook = document.querySelector(".social-img-facebook")
    const social_youtube = document.querySelector(".social-img-youtube")
    social_facebook.addEventListener("click", function () {
        window.open(FACEBOOK_URL);
    })
    social_youtube.addEventListener("click", function () {
        window.open(YOUTUBE_CHANNEL)
    })
}

function initMusicList(breathInterval, updateProgressUIInterval, breath, updateProgressUI) {

    $(".music-list-item").click(function () {
        updateSelectedSong(this.id);
        loadTrack(this.id - 1);
        // Play the loaded track
        playTrack();
    });

    const MUSIC_SOURCE_URL = 'https://meditation-web-app.s3-ap-southeast-1.amazonaws.com/meditation-music/';

    // Specify globally used values
    let track_index_global = 0;
    let isPlaying = false;
    let updateTimer;

    // Define the list of tracks that have to be played
    // Create the audio element for the player
    let curr_track = document.createElement('audio');
    // Select all the elements in the HTML page
    // and assign them to a variable
    let track_art = document.querySelector(".track-art");
    let track_name = document.querySelector(".track-name");
    let track_artist = document.querySelector(".track-artist");

    let play_pause_btn = document.querySelector(".playpause-track");
    play_pause_btn.addEventListener("click", function () {
        playPauseTrack();
    });

    let next_btn = document.querySelector(".next-track");
    next_btn.addEventListener("click", function () {
        nextTrack();
    });
    let prev_btn = document.querySelector(".prev-track");
    prev_btn.addEventListener("click", function () {
        prevTrack();
    });

    let seek_slider = document.querySelector(".seek_slider");
    seek_slider.addEventListener("input", function () {
        seekTo();
    })
    let volume_slider = document.querySelector(".volume_slider");
    volume_slider.addEventListener("input", function () {
        setVolume();
    })
    let curr_time = document.querySelector(".current-time");
    let total_duration = document.querySelector(".total-duration");

    updateSelectedSong(1);
    loadTrack(0);

    function loadTrack(track_index) {
        track_index_global = track_index;
        // Clear the previous seek timer
        clearInterval(updateTimer);
        resetValues();

        // Load a new track
        curr_track.src = MUSIC_SOURCE_URL + songs[track_index]?.source;
        curr_track.load();
        // Update details of the track
        track_art.style.backgroundImage =
            "url(" + static_url + songs[track_index].image + ")";
        track_name.textContent = songs[track_index].name;
        track_artist.textContent = songs[track_index].artist;

        // Set an interval of 1000 milliseconds
        // for updating the seek slider
        updateTimer = setInterval(seekUpdate, 1000);

        // Move to the next track if the current finishes playing
        // using the 'ended' event
        curr_track.addEventListener("ended", nextTrack);

        // Apply a random background color
        random_bg_color();
    }

    function random_bg_color() {
        // Get a random number between 64 to 256
        // (for getting lighter colors)
        let red = Math.floor(Math.random() * 256) + 64;
        let green = Math.floor(Math.random() * 256) + 64;
        let blue = Math.floor(Math.random() * 256) + 64;

        // Construct a color withe the given values
        let bgColor = "rgb(" + red + ", " + green + ", " + blue + ")";

        // Set the background to the new color
        // document.body.style.background = bgColor;
    }

    // Function to reset all values to their default
    function resetValues() {
        curr_time.textContent = "00:00";
        total_duration.textContent = "00:00";
        seek_slider.value = 0;
    }

    function playPauseTrack() {
        $(".text_breath_num").removeClass("animated_second_text");
        // Switch between playing and pausing
        // depending on the current state
        if (!isPlaying) playTrack();
        else pauseTrack();
    }

    function playTrack() {
        $(".text_breath_num").removeClass("animated_second_text");

        updateSelectedSong(track_index_global + 1)
        // Play the loaded track
        curr_track.play();
        isPlaying = true;

        // Replace icon with the pause icon
        play_pause_btn.innerHTML = '<i class="fa fa-pause-circle fa-4x"></i>';

        if (breathInterval) {
            clearInterval(breathInterval);
        }
        if (updateProgressUIInterval) {
            clearInterval(updateProgressUIInterval);
        }

        breathInterval = setInterval(breath, 100);
        updateProgressUIInterval = setInterval(updateProgressUI, 100);

    }

    function pauseTrack() {
        // Pause the loaded track
        curr_track.pause();
        isPlaying = false;

        // Replace icon with the play icon
        play_pause_btn.innerHTML = '<i class="fa fa-play-circle fa-4x"></i>';

        if (breathInterval) {
            clearInterval(breathInterval);
        }
        if (updateProgressUIInterval) {
            clearInterval(updateProgressUIInterval);
        }
    }

    function nextTrack() {
        // Go back to the first track if the
        // current one is the last in the track list
        if (track_index_global < songs.length - 1)
            track_index_global += 1;
        else track_index_global = 0;

        updateSelectedSong(track_index_global + 1);

        // Load and play the new track
        loadTrack(track_index_global);
        playTrack();
    }

    function prevTrack() {
        // Go back to the last track if the
        // current one is the first in the track list
        if (track_index_global > 0)
            track_index_global -= 1;
        else track_index_global = songs.length - 1;

        updateSelectedSong(track_index_global + 1);

        // Load and play the new track
        loadTrack(track_index_global);
        playTrack();
    }

    function seekTo() {
        // Calculate the seek position by the
        // percentage of the seek slider
        // and get the relative duration to the track
        // Set the current track position to the calculated seek position
        curr_track.currentTime = curr_track.duration * (seek_slider.value / 100)

    }

    function setVolume() {
        // Set the volume according to the
        // percentage of the volume slider set
        curr_track.volume = volume_slider.value / 100;
    }

    function seekUpdate() {
        let seekPosition = 0;

        // Check if the current track duration is a legible number
        if (!isNaN(curr_track.duration)) {
            seekPosition = curr_track.currentTime * (100 / curr_track.duration);
            seek_slider.value = seekPosition;

            // Calculate the time left and the total duration
            let currentMinutes = Math.floor(curr_track.currentTime / 60);
            let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60);
            let durationMinutes = Math.floor(curr_track.duration / 60);
            let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60);

            // Add a zero to the single digit time values
            if (currentSeconds < 10) {
                currentSeconds = "0" + currentSeconds;
            }
            if (durationSeconds < 10) {
                durationSeconds = "0" + durationSeconds;
            }
            if (currentMinutes < 10) {
                currentMinutes = "0" + currentMinutes;
            }
            if (durationMinutes < 10) {
                durationMinutes = "0" + durationMinutes;
            }

            // Display the updated duration
            curr_time.textContent = currentMinutes + ":" + currentSeconds;
            total_duration.textContent = durationMinutes + ":" + durationSeconds;
        }
    }

    function updateSelectedSong(id) {
        // Select all list items
        const listItems = $(".music-list-item");
        // Remove 'active' tag for all list items
        for (let i = 0; i < listItems.length; i++) {
            listItems[i].classList.remove("active");
            if (listItems[i].id == id) {
                listItems[i].classList.add("active")
            }
        }
    }
}


function initBreath() {
    hold_in_progress = $(".progress-hold-in");
    hold_out_progress = $(".progress-hold-out");
    hold_breath_progress = $('.progress-breath')

    text_breath_num = document.querySelector(".text_breath_num");
    text_breath_title = document.querySelector(".text_breath_title");

    // 0  stand by | 1 breath in | 2 hold in | 3 breath out | 4 hold out
    // define first progress UI
    hold_breath_progress.css('width', 100 + '%').attr('aria-valuenow', 100);
    hold_in_progress.css('width', 0 + '%').attr('aria-valuenow', 0);
    hold_out_progress.css('width', 0 + '%').attr('aria-valuenow', 0);

}

function initSoundList() {

    const SOUND_SOURCE_URL = 'https://meditation-web-app.s3-ap-southeast-1.amazonaws.com/meditation-sounds/';

    let soundObj = {};
    $(".sound-name-item").click(function () {
        const id = this.id.split('_')[1];
        const slider_div = document.querySelector(".slider_sound_div_" + id);

        const slider = slider_div.querySelector("input");

        if (_.includes(this.classList, "active")) {
            this.classList.remove("active")
            slider_div.classList.add("hide")
            soundObj[this.id].pause();
            soundObj[this.id].remove();
        } else {
            this.classList.add("active");
            slider_div.classList.remove("hide")

            // create sound element
            let curr_sound = document.createElement('audio');
            curr_sound.classList.add(this.id)
            curr_sound.loop = true;
            curr_sound.src = SOUND_SOURCE_URL + sounds[id - 1]?.source;
            curr_sound.load();
            curr_sound.play();
            soundObj[this.id] = curr_sound;

            slider.addEventListener("input", function (event) {
                curr_sound.volume = this.value / 100;
            })
        }
    });
}

function initTheme() {
    let themeLocal = localStorage.getItem('theme');
    if (themeLocal == null) {
        setTheme('light');
    } else {
        setTheme(themeLocal);
    }

    let them_dot = document.getElementsByClassName('theme-dot');
    for (let i = 0; them_dot.length > i; i++) {
        them_dot[i].addEventListener('click', evt => {
            let mode = them_dot[i].dataset.mode;
            setTheme(mode);
        })
    }
}


function setTheme(mode) {
    let theme = document.getElementById('theme-style');
    if (mode == 'light') {
        theme.href = static_url + 'meditation/css/default.css';
    }

    if (mode == 'blue') {
        theme.href = static_url + 'meditation/css/blue.css';
    }

    if (mode == 'green') {
        theme.href = static_url + 'meditation/css/green.css';
    }

    if (mode == 'purple') {
        theme.href = static_url + 'meditation/css/purple.css';
    }
    localStorage.setItem('theme', mode);

}
