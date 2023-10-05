# 🤖 SeleniumGPT: An experimental Selenium E2E Test Generator 
Forked from the Amazing ChromeGPT agent:
https://github.com/richardyc/Chrome-GPT

CREDIT WHERE CREDIT IS DUE WITHOUT HIM I COULD NOT HAVE MADE THIS THANK YOU!
https://github.com/richardyc
 
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/RealRichomie.svg?style=social&label=Follow%20%40RealRichomie)](https://twitter.com/RealRichomie)

⚠️This is an experimental AutoGPT agent that might take incorrect actions and could lead to serious consequences. Please use it at your own discretion⚠️

SeleniumGPT is an AutoGPT experiment that utilizes [Langchain](https://github.com/hwchase17/langchain) and [Selenium](https://github.com/SeleniumHQ/selenium) to enable an AutoGPT agent take control of an entire Chrome session. With the ability to interactively scroll, click, and input text on web pages, the AutoGPT agent can navigate and manipulate web content. 

This fork takes it a step further and allows you GENERATE END-TO-END TESTS ALONG THE WAY

<h2 align="center"> 🖥️ Demo </h2>

[![Video](https://img.youtube.com/vi/cxoUJwIozPI/maxresdefault.jpg)](https://www.youtube.com/watch?v=cxoUJwIozPI)

Input Prompt: `Go to BestBuy and Search for a Nintendo Switch and Add it to your Cart. Your Task is Complete after adding to Cart.`



Demo made by [Stefan Ayala](https://www.youtube.com/@Basecase_/featured)

<h2 align="center"> 🧱 Known Limitations </h2>

- There are limited web crawling features, with buttons and input fields sometimes failing to appear in prompt.
- The response time is slow, with each action taking between 1-10 seconds to run.
- At times, langchain agents are unable to parse GPT outputs (refer to langchain discussion: https://github.com/hwchase17/langchain/discussions/4065). If you run into this, try specifying a different agent; ie: `python -m chromegpt -a auto-gpt -v -t "{your request}"
- EXTREMELY EXPERIMENTAL

<h2 align="center"> Requirements </h2>

- Chrome
- Python >3.8
- Install [Poetry](https://python-poetry.org/docs/#installation)

<h2 align="center"> 🛠️ Setup </h2>

1. Set up your OpenAI [API Keys](https://platform.openai.com/account/api-keys) and add `OPENAI_API_KEY` env variable
2. Install Python requirements via poetry `poetry install`
3. Open a poetry shell `poetry shell`
4. Run chromegpt via `python -m chromegpt`

<h2 align="center"> 🧠 Usage </h2>

- GPT-3.5 Usage (Default): `python -m chromegpt -v -t "{your request}"`
- GPT-4 Usage (Recommended, needs GPT-4 access): `python -m chromegpt -v -a auto-gpt -m gpt-4 -t "{your request}"`
- For help: `python -m chromegpt --help`
```
Usage: python -m chromegpt [OPTIONS]

  Run ChromeGPT: An AutoGPT agent that interacts with Chrome

Options:
  -t, --task TEXT                 The task to execute  [required]
  -a, --agent [auto-gpt|baby-agi|zero-shot]
                                  The agent type to use
  -m, --model TEXT                The model to use
  --headless                      Run in headless mode
  -v, --verbose                   Run in verbose mode
  --human-in-loop                 Run in human-in-loop mode, only available
                                  when using auto-gpt agent
  --help                          Show this message and exit.
```

