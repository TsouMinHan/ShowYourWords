# ShowYourWords

這個專案是為了輔導的聽障生而製作的。

使用Google API將聲音轉成文字。

目前提供中文、日文、英文，三種語言。

你可以在[Google API language support](https://cloud.google.com/speech-to-text/docs/languages)挑選所需的語言，並將該語言對應的`BCP-47`寫入`languages.json`中。

目前程式還有改進的部分，當程式在翻譯時無法抓取聲音，這個問題應該可以透過Queue和Threading解決。

For the hearing impaired. Show what you are talking about.

Translate spoken words to text via Google API.

Now just for Chinese, Japanese and English.

You can get `BCP-47` code in [Google API language support](https://cloud.google.com/speech-to-text/docs/languages) and add it in `languages.json`.

The programe still has some features that can be improved.

When the API translating, programe can't track what are you saying.

I think queue or threading can fix up this issue, but i'm a lazy guy.

![](./img/1.JPG)
