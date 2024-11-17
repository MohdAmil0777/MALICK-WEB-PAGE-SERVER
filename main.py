from flask import Flask, request, render_template_string
import requests
import os
from time import sleep
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        if token_type == 'single':
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {access_token}: {message}")
                    print(e)
                    time.sleep(30)

        elif token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode().splitlines()
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for token in tokens:
                        for message1 in messages:
                            api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                            message = str(mn) + ' ' + message1
                            parameters = {'access_token': token, 'message': message}
                            response = requests.post(api_url, data=parameters, headers=headers)
                            if response.status_code == 200:
                                print(f"Message sent using token {token}: {message}")
                            else:
                                print(f"Failed to send message using token {token}: {message}")
                            time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {token}: {message}")
                    print(e)
                    time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L3G3ND M9L|CK |NS|D3</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: red;
    }
    .container{
      max-width: 300px;
      background-color: black and white;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red, green, blue, alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁
                                     ENJOY GYS SHAH KHAN KI MKC SE NIKLA OFFLINE SERVER 😈  >3:)
    <h1 class="mt-3">🅾🆆🅽🅴🆁]|I{•------» SHAH KHAN KA FATHER M9L|CK |NS|D3🗿✅  </h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI MKC LEGA YA SATH MAI GAAND BHI LEGA SELECT KAR:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI MKC</option>
          <option value="multi">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI MKC + & GAAND</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI DIDI KI XCHUT MA JANE WALA LUND DAL:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId"> (𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI MKC KA ADDRESS DAL:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI SEXY DIDI KA NAME DAL:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI DIDI KI GAND FHADNE WALI GALI DAL:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">(𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍) KI DIDI KO CHODNE KI SPEED DAL :</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by (𝐒𝐇𝐀𝐇 𝐊𝐇𝐀𝐍 𝐊𝐀 𝐅𝐀𝐓𝐇𝐄𝐑 𝐌𝐀𝐋𝐈𝐂𝐊 𝐈𝐍𝐒𝐈𝐃𝐄) 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <a href="https://github.com/zeeshanqureshi0">GitHub</a></p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    });
  </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
