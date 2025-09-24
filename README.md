# SnipLink - A Simple & Modern URL Shortener

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-orange.svg)](https://flask.palletsprojects.com/)

SnipLink is a lightweight and efficient URL shortening service built with Python and Flask. It provides a clean, modern user interface to transform long, unwieldy links into short, memorable ones.



---

## ## ✨ Key Features

-   **Shorten URLs:** Quickly generate a unique, 7-character short code for any valid URL.
-   **Seamless Redirection:** Short links automatically and instantly redirect to their original long URL.
-   **Clean & Responsive UI:** A modern, user-friendly interface that works beautifully on both desktop and mobile devices.
-   **Persistent Storage:** Uses SQLite for simple local development and is configured for a robust PostgreSQL database in production.
-   **Duplicate Prevention:** If a URL has already been shortened, the system returns the existing short link instead of creating a new one.

---

## ## 🚀 Tech Stack

-   **Backend:** Python, Flask
-   **Frontend:** HTML5, CSS3
-   **Database:**
    -   **Development:** SQLite
    -   **Production:** PostgreSQL (via Neon)
-   **Deployment:** Gunicorn, Render

---

## ## Local Development Setup

Follow these steps to get the project running on your local machine.

#### **1. Prerequisites**

-   [Python 3.9+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/)

#### **2. Clone the Repository**

```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name