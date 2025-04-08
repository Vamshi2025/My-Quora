# My Quora (Django)

A mini Quora-style web app where users can:

- Register/Login
- Post questions
- Answer others' questions
- Like answers
- Logout

## How to Run

```bash
git clone <your-repo-url>
cd my_quora

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
