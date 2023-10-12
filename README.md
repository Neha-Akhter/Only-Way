
# The Only Way

The "The Only Way" website is a comprehensive platform designed for individuals interested in Islam. It offers authenticated login and registration, allowing users to access a wide range of resources related to Islam. Users can explore Quranic Verses and Ahadith relevant to daily life, access various blogs on Islamic topics, and even participate in daily quizzes to test their knowledge. Additionally, the platform includes an e-store where users can purchase items such as Quranic copies, tasbihs, canvas frames, miswak, and more. This project caters to anyone seeking information, knowledge, and products related to Islam.



## Features

- A common user will be able to register himself/herself which will allow him/her to make purchases from our platform.
- Selection of Quranic Verses based on topic/feelings along with translation.
- Selection of Ahadith based on specific topic/feelings along with translation.
- Searching of article/blogs covering the common and popular aspects of Islam.
- Increasing general Islamic knowledge by taking daily quiz.
- Visiting our e-commerce store.
- Buying article(s) and proceeding to checkout to make payments.


## Tech Stack


**Frontend:** HTML, CSS, Bootstrap, Django(Python)

**Backend:** MySQL

**Tool:** VS Code



## Installation

### 1. Clone the repository

First, clone this repository:

```bash
  git clone https://github.com/Neha-Akhter/Only-Way.git
  cd Only-Way
```
### 2. Create a virtual environment

```bash
  virtualenv myenv
  source myenv/bin/activate
```

### 3. Install project dependencies

```bash
  pip install -r requirements.txt
```

### 4. Configure database and apply migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```
### 5. Run the application on local server

```bash
  python manage.py runserver
```
