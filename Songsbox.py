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
            margin-bottom: 15px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
            text-align: left;
        }
        li {
            padding: 10px;
            margin-bottom: 5px;
            background: #eee;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.2s; 
            color: #333;
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
        <h3 style="color: #333;">သီချင်းစာရင်း (Playlist)</h3>
        <audio id="audioPlayer" controls></audio>
        <ul id="playlist"></ul>
    </div>

    <script>
        const songs = [
            {
                title: "အပြုံးကိုအပြီးဌားခဲ့.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AF%E1%80%B6%E1%80%B8%E1%80%80%E1%80%AD%E1%80%AF%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AE%E1%80%B8%E1%80%8C%E1%80%AC%E1%80%B8%E1%80%81%E1%80%B2%E1%80%B7.mp3"
            },
            {
                title:"ဆေးလိပ်နဲ့မီးခြစ်.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%86%E1%80%B1%E1%80%B8%E1%80%9C%E1%80%AD%E1%80%95%E1%80%BA%E1%80%94%E1%80%B2%E1%80%B7%E1%80%99%E1%80%AE%E1%80%B8%E1%80%81%E1%80%BC%E1%80%85%E1%80%BA.mp3"
            },
            {
                title:"ပြတ်တုန်းလပ်တုန်း.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%95%E1%80%BC%E1%80%90%E1%80%BA%E1%80%90%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%E1%80%9C%E1%80%95%E1%80%BA%E1%80%90%E1%80%AF%E1%80%94%E1%80%BA%E1%80%B8%2023.mp3"
            },
            {
                title:"ပြတ်တုန်းလပ်တုန်း.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%90%E1%80%B1%E1%80%AC%E1%80%BA%E1%80%9B%E1%80%AC.mp3"
            }
        ];

        const audioPlayer = document.getElementById('audioPlayer');
        const playlistElement = document.getElementById('playlist');

        function loadPlaylist() {
            songs.forEach((song, index) => {
                let li = document.createElement('li');
                li.textContent = (index + 1) + ". " + song.title;
                li.addEventListener('click', () => {
                    playSong(index);
                });
                playlistElement.appendChild(li);
            });
        }

        function playSong(index) {
            audioPlayer.src = songs[index].src;
            audioPlayer.load();
            audioPlayer.play().catch(error => {
                console.log("Play blocked:", error);
            });
            
            document.querySelectorAll('#playlist li').forEach((li, idx) => {
                if (idx === index) {
                    li.classList.add('active');
                } else {
                    li.classList.remove('active');
                }
            });
        }

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

st.components.v1.html(html_code, height=400)
