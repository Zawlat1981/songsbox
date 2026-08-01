import streamlit as st

# Streamlit App ရဲ့ ခေါင်းစဉ်
st.title("My Song Playlist App")

# HTML ကုဒ်များကို ဒီထဲမှာ တိုက်ရိုက်ထည့်ပါ
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
        <h3>သီချင်းစာရင်း (Playlist)</h3>
        <audio id="audioPlayer" controls></audio>
        <ul id="playlist"></ul>
    </div>

    <script>
        const songs = [
            {
                title: "အပြုံးကိုအပြီးဌားခဲ့.mp3",
                src: "https://github.com/Zawlat1981/my-audio/raw/refs/heads/main/%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AF%E1%80%B6%E1%80%80%E1%80%AD%E1%80%AF%E1%80%A1%E1%80%95%E1%80%BC%E1%80%AE%E1%80%B8%E1%80%8C%E1%80%AC%E1%80%B8%E1%80%81%E1%80%B2%E1%80%B7.mp3"
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
            audioPlayer.play();
            document.querySelectorAll('#playlist li').forEach((li, idx) => {
                if (idx === index) {
                    li.classList.add('active');
                } else {
                    li.classList.remove('active');
                }
            });
        }

        loadPlaylist();
        if(songs.length > 0) {
            audioPlayer.src = songs[0].src;
            playlistElement.children[0].classList.add('active');
        }
    </script>

</body>
</html>
"""

# Streamlit မှာ HTML ကို ပြသရန်
st.components.v1.html(html_code, height=400)