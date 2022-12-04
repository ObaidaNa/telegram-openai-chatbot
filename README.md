
<a name="readme-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">telegram-openai-chatbot</h1>

  <p align="center">
    <a href="https://t.me/Alphauserbot_bot">View Demo (it may be dead)</a>
    ·
    <a href="https://github.com/ObaidaNa/telegram-openai-chatbot/issues">Report Bug</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

This is a very simple chatbot which is dealing with <a href="https://openai.com/"> OpenAi </a> API 


### Built With

* [Python](python.org)
* <a href="https://docs.pyrogram.org/"> Pyrogram </a>
* <a href="https://openai.com/"> OpenAi </a>


<!-- GETTING STARTED -->
## Getting Started

The idea of this bot is only chating with you, follow the instructions below to deploy and use it

### Prerequisites

* Get a free API Key from [OpenAi](https://beta.openai.com/account/api-keys)

* Get `API_HASH` and `API_ID` from  [here](https://my.telegram.org/) and get `BOT_TOKEN` from [Botfather](https://t.me/BotFather)

* Add `OPENAI_API_KEY`, `API_HASH`, `API_ID` to `.env` file


### Installation

1.  Clone the repo:
   ```sh
   git clone https://github.com/ObaidaNa/telegram-openai-chatbot.git
   ```
   Change directory:
   ```sh
   cd telegram-openai-chatbot
   ```
   then install requirements:
   ```sh
   pip install -r requirements.txt
   ```
   
2. Generate session string using by running:
```sh
python generate_session_str.py
```
   
3. Copy the session string and past it in `STRING_SESSION` in `.env` file



<!-- USAGE EXAMPLES -->
## Usage
Simply run the main.py file:
```sh
python main.py
```
and enjoy the AI chatbot ;)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

[@ObaidaNa](https://t.me/ObaidaNa) - obaidana@protonmail.com



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
