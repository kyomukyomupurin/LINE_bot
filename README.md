# LINE_bot

LINE notify で Codeforces の API を叩いた結果を通知してくれる bot 。

## ```codeforces.py```

レーティングが Highest からどれだけ下がったか教えてくれる。```python3 codeforces.py user_name``` のように実行する。

## ```contest_info.py```

今後のコンテスト予定を教えてくれる。

## ```blog_info.py```

新しく投稿されたブログの URL を教えてくれる。最新のブログの投稿 ID を ```last_blogEntryId.txt``` に保存している。