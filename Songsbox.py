import streamlit as st

st.title("My Song Playlist App")

html_code = """
<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <style>
        .player-box {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            width: 320px;
            text-align: center;
        }
        audio {
            width: 100%;
            margin-bottom: 10px;
        }
        .controls-panel {
            margin-bottom: 15px;
            text-align: left;
            font-size: 13px;
            color: #333;
        }
        .controls-panel select {
            width: 100%;
            padding: 6px;
            border-radius: 5px;
            border: 1px solid #ccc;
            margin-top: 5px;
            font-size: 13px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
            text-align: left;
            max-height: 200px;
            overflow-y: auto;
        }
        li {
            padding: 8px 10px;
            margin-bottom: 5px;
            background: #eee;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.2s; 
            color: #333;
            font-size: 14px;
        }
        li:hover {
            background: #ddd;
        }
        li.active {
            background: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>

    <div class="player-box">
        <h3 style="color: #333; margin-top: 0;">သီချင်းစာရင်း (Playlist)</h3>
        
        <div class="controls-panel">
            <label for="playMode"><b>ဖွင့်မည့်ပုံစံ (Play Mode):</b></label>
            <select id="playMode">
                <option value="sequence">➡️ အစဉ်လိုက်ဖွင့်မည် (Sequence)</option>
                <option value="repeatOne">🔂 ဒီတစ်ပုဒ်တည်း ထပ်ကာထပ်ကာဖွင့်မည် (Repeat One)</option>
                <option value="shuffle">🔀 ဟိုတစ်ပုဒ် ဒီတစ်ပုဒ် ကျော်၍ဖွင့်မည် (Shuffle)</option>
            </select>
        </div>

        <audio id="audioPlayer" controls></audio>
        <ul id="playlist"></ul>
    </div>

    <script>
        const songs = [
            {
                title: "အပြုံးကိုအပြီးဌားခဲ့.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AF%E1%80%B6%E1%80%80%E1%80%AD%E1%80%AF%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AE%E1%80%B8%E1%80%8C%E1%80%AC%E1%80%B8%E1%80%81%E1%80%B2%E1%80%B7.mp3"
            },
            {
                title: "ဆေးလိပ်နဲ့မီးခြစ်.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%86%E1%80%B1%E1%80%B8%E1%80%9C%E1%80%AD%E1%80%95%E1%80%BA%E1%80%94%E1%80%B2%E1%80%B7%E1%80%99%E1%80%AE%E1%80%B8%E1%80%81%E1%80%BC%E1%80%85%E1%80%BA.mp3"
            },
            {
                title: "ပြတ်တုန်းလပ်တုန်း.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%95%E1%80%BC%E1%80%90%E1%80%BA%E1%80%90%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%E1%80%9C%E1%80%95%E1%80%BA%E1%80%90%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%2023.mp3"
            },
            {
                title: "တော်ရာ.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%90%E1%80%B1%E1%80%AC%E1%80%BA%E1%80%9B%E1%80%AC.mp3"
            }
        ];

        const audioPlayer = document.getElementById('audioPlayer');
        const playlistElement = document.getElementById('playlist');
        const playModeSelect = document.getElementById('playMode');
        
        let currentIndex = 0;

        function loadPlaylist() {
            songs.forEach((song, index) => {
                let li = document.createElement('li');
                li.textContent = (index + 1) + ". " + song.title;
                li.addEventListener('click', () => {
                    currentIndex = index;
                    playSong(currentIndex);
                });
                playlistElement.appendChild(li);
            });
        }

        function playSong(index) {
            currentIndex = index;
            audioPlayer.src = songs[currentIndex].src;
            audioPlayer.load();
            audioPlayer.play().catch(error => {
                console.log("Play blocked:", error);
            });
            
            document.querySelectorAll('#playlist li').forEach((li, idx) => {
                if (idx === currentIndex) {
                    li.classList.add('active');
                    li.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } else {
                    li.classList.remove('active');
                }
            });
        }

        // သီချင်းတစ်ပုဒ် ပြီးဆုံးသွားသည့်အခါ လုပ်ဆောင်မည့် အပိုင်း (Auto Next)
        audioPlayer.addEventListener('ended', () => {
            const mode = playModeSelect.value;

            if (mode === 'repeatOne') {
                // ဒီတစ်ပုဒ်တည်းကို ပြန်ဖွင့်မည်
                audioPlayer.currentTime = 0;
                audioPlayer.play();
            } else if (mode === 'shuffle') {
                // ဟိုတစ်ပုဒ် ဒီတစ်ပုဒ် ကျပန်းရွေးမည် (လက်ရှိသီချင်းနဲ့ မတူတာကို ရွေးရန်)
                let nextIdx;
                if (songs.length > 1) {
                    do {
                        nextIdx = Math.floor(Math.random() * songs.length);
                    } while (nextIdx === currentIndex);
                } else {
                    nextIdx = 0;
                }
                playSong(nextIdx);
            } else {
                // အစဉ်လိုက် (နောက်တစ်ပုဒ်ကို ကူးမည်၊ ပြီးသွားရင် ပထမဆုံးကို ပြန်စမည်)
                currentIndex = (currentIndex + 1) % songs.length;
                playSong(currentIndex);
            }
        });

        loadPlaylist();
        
        // ပထမစဝင်လာချင်း ပထမသီချင်းကို Source ထည့်ပေးထားမည် (Autoplay မလုပ်ပါ)
        if(songs.length > 0) {
            audioPlayer.src = songs[0].src;
            document.querySelectorAll('#playlist li')[0].classList.add('active');
        }
    </script>

</body>
</html>
"""

st.components.v1.html(html_code, height=450)
