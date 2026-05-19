# バックアップフォルダ

Seal Subscriptions で既存メールテンプレートを差し替える前に、
**現行のEmail body (HTML) 全文をコピーしてこのフォルダに保存**してください。

## 命名規則

`original-XX-<メール名>.html`

例:
- `original-03-billing-succeeded.html`
- `original-11-shipping-updated.html`

## ロールバック方法

もし新テンプレで問題が発生したら：
1. このフォルダの該当ファイルを開く
2. 全文コピー
3. Seal管理画面の Email body (HTML) に貼り直す
4. Save

これで即座に元のデザインに戻せます。

## チェックリスト進捗管理

各メールのステータスは以下の表で管理してください（手動更新）。

| # | メール | バックアップ | 貼り替え | Preview | Test送信 | 受信確認 | 本番Save | 状態 |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 11 | Shipping updated | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 12 | Payment updated | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 09 | Expired | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 06 | Resumed | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 05 | Paused | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 08 | Skipped | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 10 | 24h前発送 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 01 | Subscription created | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 02 | Upcoming reminder | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 07 | Cancelled | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 03 | Billing succeeded | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
| 04 | Billing failed | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 未着手 |
