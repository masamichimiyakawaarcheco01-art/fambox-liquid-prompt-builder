# Seal Subscriptions メールテンプレート運用ガイド

FAM BOX・FAM アスリート食トレの定期便通知メールを、FAM ブランド DNA で統一刷新するための運用ガイド。
設計書は [`docs/superpowers/specs/2026-04-22-seal-subscription-email-design.md`](../../../../docs/superpowers/specs/2026-04-22-seal-subscription-email-design.md) を参照。

---

## 1. 事前準備：ロゴを Shopify Files にアップロード

プロトタイプではローカル画像（`file:///Users/archecoinc./LMLT_FAMBOX_Black.png`）を参照しているが、
本番のメールテンプレートでは Shopify Files 配信の CDN URL に差し替える必要がある。

### 手順
1. Shopify 管理画面 → **設定 (Settings)** → **ファイル (Files)** を開く
2. 右上「**ファイルをアップロード**」から `LMLT_FAMBOX_Black.png` をアップ
3. アップロード後、ファイル一覧で対象ファイル横のクリップアイコンをクリックして**CDN URL をコピー**
   （例：`https://cdn.shopify.com/s/files/1/XXXX/YYYY/files/LMLT_FAMBOX_Black.png`）
4. 同じ手順で `LMLT_FAM_Black.png`（FAM アスリート食トレ用）もアップ

### ロゴ配信時の注意
- **黒単色 PNG** を使う → Apple Mail / iOS Mail のダークモード反転で自動的に白抜きされる
- **透過 PNG** → 背景色に依存しない
- **Retina 対応** → 2 倍サイズ（240×56px 等）をアップして `width="120" height="28"` でダウンスケール表示
- 容量目安 **30KB 以下**（大きすぎると Gmail で画像が自動ブロックされる可能性）

---

## 2. Seal Subscriptions 管理画面でメールテンプレートを変更する

### 2.1 編集画面までの導線
1. Shopify 管理画面 → 左サイドバー「**アプリ**」→ **Seal Subscriptions** をクリック
2. Seal 内の左サイドバー → **Settings** をクリック
3. 上部のタブから「**Notifications**」または「**Notifications & Emails**」を選択
4. 編集したい通知種別（例：`Recurring order confirmation` / `Upcoming billing reminder` 等）をクリック

### 2.2 編集画面の構成
各メールテンプレートには次のフィールドがある：

| フィールド | 編集内容 |
|---|---|
| **Enabled** | このメールの送信 ON/OFF |
| **Subject** | 件名。Liquid 変数 `{{ customer.first_name }}` 等が使える |
| **Preheader / Preview text** | 受信箱プレビューに表示される短文 |
| **Email body (HTML)** | メール本文の HTML ソース（ここを全面差し替え） |
| **Send delay** | 送信タイミング（リマインドの場合：決済 N 日前） |

### 2.3 差し替え手順（1 種類あたり）
1. 対象メールを開く
2. **Email body (HTML)** フィールドの既存 HTML をすべて選択して削除
3. `projects/fambox/emails/seal/XX-*.html` の該当ファイルを開き、全文をコピー
4. Seal の Email body フィールドに貼り付け
5. **Subject** も設計書 4.2 節の文案に差し替え
6. **Preheader** も差し替え
7. ロゴ `<img src="file:///...">` を **Shopify Files の CDN URL**に置換（検索→置換）
8. CTA の `href="https://fambox.example.com/account/subscriptions"` を **Seal の実際のマイページ URL**に置換（Seal 変数 `{{ subscription.manage_url }}` が使えればそれを使う）
9. 商品画像プレースホルダ `<div style="width:64px;height:64px;background:#ECECEC..."></div>` を **Liquid ループ**に置換（下記 2.4 参照）
10. ハードコードしたサンプル値（「マサミチ ミヤカワ」「#1024」「¥950」等）を **Liquid 変数**に置換
11. **Save** で保存
12. **Preview email** ボタンでプレビュー確認
13. **Send test email** で自分宛にテスト送信し、複数クライアント（Gmail Web/iOS、Apple Mail、Outlook）で確認

### 2.4 ハードコードから Liquid 変数への置換対応表
| プロトタイプのハードコード値 | Seal の Liquid 変数に置換 |
|---|---|
| `マサミチ ミヤカワ 様` | `{{ customer.first_name }} {{ customer.last_name }} 様` |
| `#1024` | `#{{ order.number }}` |
| `【おまかせ定期便】ヘルスケアプラン30...` | `{{ line_item.title }}` |
| `1食 / 週1回　×　1` | `{{ line_item.variant_title }}　×　{{ line_item.quantity }}` |
| `¥950`（商品単価） | `{{ line_item.price \| money_without_trailing_zeros }}` |
| `¥950`（小計） | `{{ subtotal_price \| money_without_trailing_zeros }}` |
| `¥1,088`（送料） | `{{ shipping_price \| money_without_trailing_zeros }}` |
| `¥2,038`（合計） | `{{ total_price \| money_without_trailing_zeros }}` |
| 商品画像プレースホルダ（`<div>`） | `<img src="{{ line_item.image \| img_url: '128x128', crop: 'center' }}" width="64" height="64" style="display:block;border-radius:8px;">` |
| `fam.athletefood.frozen@gmail.com` | `{{ shop.email }}` |

**注意**：Seal と Shopify 標準通知で変数名が微妙に違う場合がある。
Seal の編集画面に「使える変数一覧」が右サイドに表示されるので、そこを見て正しい変数名に置き換えること。

### 2.5 商品複数行のループ（Liquid）
プロトタイプでは商品 1 行だけハードコードしているが、実装時は `line_items` 配列を `{% for %}` でループ：

```liquid
{% for line_item in line_items %}
<tr>
  <td style="padding:20px 24px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td width="64" valign="top" style="width:64px;">
          <img src="{{ line_item.image | img_url: '128x128', crop: 'center' }}" alt="" width="64" height="64" style="display:block;border-radius:8px;">
        </td>
        <td width="16" style="width:16px;">&nbsp;</td>
        <td valign="top">
          <p class="fam-item-title" style="margin:0 0 4px 0;font-family:'Hiragino Kaku Gothic ProN','Hiragino Sans',sans-serif;font-size:15px;font-weight:600;line-height:1.5;color:#1B1D1A;">
            {{ line_item.title }}
          </p>
          <p style="margin:0;font-family:'Hiragino Kaku Gothic ProN','Hiragino Sans',sans-serif;font-size:13px;font-weight:400;line-height:1.5;color:#888888;">
            {{ line_item.variant_title }}　×　{{ line_item.quantity }}
          </p>
        </td>
        <td align="right" valign="top" style="font-family:'Helvetica Neue',Arial,sans-serif;font-size:15px;font-weight:600;color:#1B1D1A;white-space:nowrap;">
          {{ line_item.price | money_without_trailing_zeros }}
        </td>
      </tr>
    </table>
  </td>
</tr>
{% unless forloop.last %}
  <tr><td style="padding:0 24px;"><div style="height:1px;background:#ECECEC;line-height:1px;font-size:0;">&nbsp;</div></td></tr>
{% endunless %}
{% endfor %}
```

---

## 3. テスト送信による検証

### 3.1 Seal のプレビュー機能
- Settings → Notifications → 対象メール → **Preview e-mail** ボタン
- ブラウザ上で実データ込みのプレビューが開く
- Liquid 変数が正しく描画されるかをここで確認

### 3.2 実メール送信テスト
- Seal の **Send test email** ボタンで管理者アドレスに送信
- 複数のメールクライアントで受信して確認：
  - **Gmail Web** — ライトモード／ダークモード
  - **Gmail iOS アプリ** — ライトモード／ダークモード
  - **Apple Mail（Mac）** — ライトモード／ダークモード
  - **iOS Mail** — 既定アプリ
  - **Outlook Web** — できれば Windows 版も
- チェック項目：
  - ロゴが表示される（画像ブロック時は alt テキスト「FAMBOX」が出る）
  - Drive Orange の CTA ボタンが正しくレンダリング（Outlook は VML フォールバック）
  - 金額が `¥950` 表記になっている（`950.00 JPY` になっていない）
  - 日本語フォントが化けていない
  - レイアウトが 600px 幅で破綻していない
  - SP で横スクロールが発生していない
  - ダークモード時に白背景のまま表示される（反転していない）

### 3.3 実データでのテスト
- テスト環境に実際の定期便を 1 件作成（自分のメールアドレスで登録）
- 決済成功・失敗・スキップ・解約のシナリオを順に実行
- 各シナリオで届いたメールを確認

---

## 4. 作業順序の推奨

1. **Billing attempt succeeded（決済完了）** — プロトタイプ完成済み。最初にこれを Seal に投入し、検証 OK なら共通パーツが確定
2. **Billing attempt failed（決済失敗）** — コア体験。装飾だけ差分（アクセント帯 → 赤）
3. **Upcoming billing reminder（次回予告）** — コア体験
4. **Subscription created（定期便開始）** — 初回オンボーディング
5. **Subscription cancelled（解約）** — 出口体験
6. 残り 7 種（Paused / Resumed / Skipped / Expired / 24h before / Shipping updated / Payment updated）を連続投入

---

## 5. 運用のコツ

- **共通パーツ更新時は全 12 ファイルを再投入**。Seal にはパーシャル機能がないため、ヘッダーを 1 箇所変えたいだけでも全ファイルの貼り直しが必要
- ローカルの `projects/fambox/emails/seal/` が**唯一のソース**。Seal 管理画面で直接編集しない（ローカルとズレる）
- 変更時は必ず git commit。どのメールをいつ更新したか追える
- テスト送信で問題が見つかったらローカル HTML を修正 → 再投入
- FAMBOX / FAM アスリート食トレ でブランド分岐が必要になったら、ロゴ CDN URL だけを差し替えた**同一テンプレートの 2 セット運用**を推奨（設計書 8 節参照）

---

## 6. 既知の制限

- Seal のメールテンプレート HTML 入力欄に**文字数制限**がある場合がある（大量のインラインスタイルで hit する可能性）→ 実投入時に検証
- Outlook Desktop（Windows）ではダークモード時にピル型ステータスラベルの半透明色が潰れる可能性 → VML で上書きが必要なら追加対応
- Gmail は `<style>` タグ内のメディアクエリをサポートするが、Yahoo Mail など一部クライアントは無視する → レスポンシブは「壊れない」ことを目標に
