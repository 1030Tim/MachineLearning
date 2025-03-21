# 這幾個月我學到的線性模型檢視

### 🔹 學習方法
觀看影片 [我阿媾都會](https://youtu.be/wm9yR1VspPs?si=6bz7dpUF0IUg6gfT)

---

## 一、 線性模型 (Linear Model)

  1. [x] Simple Linear Regression
  2. [ ] Multiple Linear Regression
      - [ ] 計算梯度時出錯
  3. [ ] Logistic Regression (未實作)

## 二、 優化
  1. [ ] One Hot Encoder
  2. [ ] 熱力圖找關聯性（熟練度低）
  3. [ ] MSE Cost Function
  4. [ ] Gradient Descent
        - [ ] Simple Linear Regression
        - [ ] Multiple Linear Regression 

## 三、 📌 目標
    1. 期限：一個月3/21~4/21
    2. 學習計畫：
        - 修正多元線性回歸的梯度計算錯誤
        - 實際案例多練習多實作


## 四、 🔹 核心概念
### 1. 資料呈現線性關係（直線趨勢）

### 2. 回歸方程式（Model）

  - **簡單線性回歸**（Simple Linear Regression）
\[
y = w_0 + w_1 x + \epsilon
\]

 - **多元線性回歸（Multiple Linear Regression）**
\[
y = w_0 + w_1 x_1 + w_2 x_2 + \dots + w_n x_n + \epsilon
\]

 - **邏輯迴歸（Logistic Regression）**
\[
h_w(x) = \sigma(w^T x) = \frac{1}{1 + e^{-w^T x}}
\]

### 3. 找到適合的模型，之後專注於找到最佳的參數 \( w \) 和 \( b \)可以用Gradient Descent透過斜率計算的方式找到最佳的\(w\) 與 \(b\) Cost 又為最小


---

## 五、 心得與學習過程

### 1. 💡 遇到的問題
1. **多元線性回歸**：在計算梯度時出錯，需要進一步理解其數學理論，更有效的使用更新公式。
- **邏輯回歸**：尚未實作，對於 Sigmoid 函數與交叉熵損失函數的理解還需要加強。

### 2. ✅ 解決方法
- 實作一次影片內容並找資料實際操作。
- 深度了解閱讀數學知識
- 與套件結果做比對。

## 六、 🚀 下一步計劃
- 專案實作
- 前往展開深度學習
- 類神經網路搭設

