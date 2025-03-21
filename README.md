# 這幾個月我學到的線性模型檢視

### 🔹 學習方法
觀看影片 [我阿嬤都會](https://youtu.be/wm9yR1VspPs?si=6bz7dpUF0IUg6gfT)

---

## 一、線性模型 (Linear Model)

- [x] **Simple Linear Regression**
- [ ] **Multiple Linear Regression** (計算梯度時出錯)
- [ ] **Logistic Regression** (未實作)

## 二、優化
- [ ] **One Hot Encoder**
- [ ] **熱力圖找關聯性**（熟練度低）
- [ ] **MSE Cost Function**
- [ ] **Gradient Descent**
  - [ ] Simple Linear Regression
  - [ ] Multiple Linear Regression 

---

## 三、📌 目標
### 1. 期限
📅 **3/21 ~ 4/21**

### 2. 學習計畫
- ✅ 修正多元線性回歸的梯度計算錯誤
- ✅ 實際案例多練習、多實作

---

## 四、🔹 核心概念

### 1️⃣ 資料呈現線性關係（直線趨勢）

### 2️⃣ 回歸方程式（Model）

#### 📌 簡單線性回歸（Simple Linear Regression）
$$
y =  w_0 x + b
$$

#### 📌 多元線性回歸（Multiple Linear Regression）
$$
y = w_0 + w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b
$$

#### 📌 邏輯迴歸（Logistic Regression）
$$
h_w(x) = \sigma(w^T x) = \frac{1}{1 + e^{-w^T x}}
$$

### 3️⃣ 找到適合的模型，之後專注於找到最佳的參數 \( w \) 和 \( b \)
可以用 **Gradient Descent** 透過斜率計算的方式找到最佳的 \( w \) 與 \( b \)，Cost 又為最小。

---

## 五、心得與學習過程

### 1️⃣ 💡 遇到的問題
- **多元線性回歸**：在計算梯度時出錯，需要進一步理解其數學理論，更有效地使用更新公式。
- **邏輯回歸**：尚未實作，對於 Sigmoid 函數與交叉熵損失函數的理解還需要加強。

### 2️⃣ ✅ 解決方法
- 📌 **實作**：跟著影片內容一步步操作。
- 📖 **深入學習數學**：理解公式推導過程。
- 🔍 **與現有套件結果比對**，檢查誤差。

---

## 六、🚀 下一步計劃
- 🔧 **專案實作**
- 🤖 **開始學習深度學習**
- 🧠 **類神經網路搭建**