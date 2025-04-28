<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Happy Birthday Bubuuu!</title>
  <style>
    body {
      background-color: #ffe6f0;
      font-family: 'Comic Sans MS', cursive, sans-serif;
      color: #ff3399;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      text-align: center;
      padding: 20px;
    }
    .message {
      font-size: 1.5em;
      max-width: 700px;
      line-height: 1.6;
    }
    .heart {
      font-size: 2em;
      animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.2); }
      100% { transform: scale(1); }
    }
  </style>
</head>
<body>

<div class="message" id="text"></div>

<script>
const text = `Happy 19th birthday bubuuu, ociiiwww, cinta akuuu!!!\n
Gak kerasa yaa udah 19 ajaa, makin dewasa, makin keren, makin gemesinnn — dan aku makin cinta sama kamu setiap harinyaa.\n
Aku bersyukur bangeeet bisa nemuin kamu di hidup aku. Kamu tuh kayak cahaya kecil yang masuk di sela-sela hari aku, tiba-tiba aja hidup aku jadi lebih cerah, lebih rame, lebih rame kayak pasar malam (tapi aku sukaa banget)!\n
Kadang aku ngerasa kita tuh masiii linglung sama hubungan kitaa — kadang bingung, kadang takut, kadang cuma bisa saling mandang kayak dua bocil ilang di mall... tapi serius deh, di balik semua itu, aku sayang kamu banget. Tulus. Gak main-main. Gak ada kata-kata yang cukup buat ngejelasin betapa berharganya kamu buat akuuu.\n
Semoga kita selalu bisa barengan yaa, semoga tangan kita gak lepas, kayak lem UHU super lengket (gak bisa dipisahhh).\n
Aku pengen banget kita selalu terbuka satu sama lain, gak ada yang ditahan-tahan. Mau itu cerita receh, sedih, takut, atau marah, semuaaa cerita kamu, aku mau jadi orang pertama yang tauu.\nDan aku mau kita selalu jujur yaaa, aku janji aku juga jujur kok sama kamu... sejujur-jujurnya, bahkan kalo aku kangen berat sama kamu sampai mau nangis di kasur sendirian, aku bakal jujur ngaku. (kalo malu dikit-dikit ya gapapa sihh)\n
Aku cinta banget sama kamu, sayanggg.\nTerima kasih udah hadir di hidup aku, udah jadi tempat aku ngelepas semua capek, tempat aku ketawa, tempat aku bisa jadi aku seutuhnya.\n
Selamat ulang tahun cintaku, semoga semua mimpi kamu pelan-pelan kejadian, satu-satu kayak main claw machine (tapi kali ini yang diambil semua menang yaa).\nAku bakal terus ada buat kamu, peluk kamu, genggam tangan kamu, dan jadi bocil favorit kamu sampai tua nanti.\n
Aku, Ikuu, sayang buangettt sama Bubuuu, ociiiwwwkuuuu!!!\nHappy 19th, love youu infinity muchhh!!!\n\n🥳🥳🥳🫶🫶🫶❣️❣️❣️❣️💞💞💞`;

let i = 0;
function typeWriter() {
  if (i < text.length) {
    document.getElementById("text").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, 30);
  }
}
typeWriter();
</script>

</body>
</html>
