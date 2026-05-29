# Livract — Django App Structure

Livract will be split into several Django apps.

Each app has one clear responsibility so the project stays clean, organized, and easy to maintain.

---

## 1. Global Project Structure

```txt
livract/
├── manage.py
├── livract/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── accounts/
│           ├── register.html
│           ├── login.html
│           ├── profile.html
│           └── edit_profile.html
│
├── books/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── books/
│           ├── add_book.html
│           ├── my_books.html
│           ├── book_detail.html
│           └── search_books.html
│
├── exchanges/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── exchanges/
│           ├── requests.html
│           ├── request_detail.html
│           └── create_request.html
│
├── messaging/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── messaging/
│           ├── inbox.html
│           └── conversation.html
│
├── events/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── events/
│           ├── event_list.html
│           ├── event_detail.html
│           └── create_event.html
│
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── core/
│           ├── home.html
│           └── base.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/
    ├── avatars/
    └── book_covers/
```

---

# 2. Development Steps

The application should be built step by step.

The goal is to avoid building everything at once and to make sure each feature works before moving to the next one.

---

## Step 1 — Project Setup

The first step is to create the Django project and configure the basic environment.

### Goal

Set up the main Django project and make sure the server runs correctly.

### Commands

```bash
django-admin startproject livract
cd livract
python manage.py runserver
```

### Main Tasks

* Create the Django project
* Check that the development server works
* Configure the database
* Configure `settings.py`
* Prepare the global project structure
* Create the `static/` and `media/` folders

---

# 3. Apps Overview

Livract is divided into multiple Django apps.

Each app handles a specific part of the project.

| App         | Responsibility                                  |
| ----------- | ----------------------------------------------- |
| `accounts`  | Users, authentication, profiles                 |
| `books`     | Book creation, book management, book search     |
| `exchanges` | Borrowing, lending, giving, exchanging requests |
| `messaging` | Conversations between users                     |
| `events`    | Community events                                |
| `core`      | Shared pages, homepage, base template           |

---

# 4. Accounts App

The `accounts` app should be built first because most other features depend on users.

Users must be able to register, log in, log out, and manage their profile before they can add books or make exchange requests.

---

## Step 2 — Create the Accounts App

### Command

```bash
python manage.py startapp accounts
```

---

## Accounts App Structure

```txt
accounts/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── accounts/
        ├── register.html
        ├── login.html
        ├── profile.html
        └── edit_profile.html
```

---

## Accounts Features to Build

### User System

* Custom user model
* User registration
* User login
* User logout
* User authentication

### Profile System

* Profile model
* Profile page
* Edit profile page
* Avatar upload
* User bio
* User location or city

---

## Important Files

### `accounts/models.py`

This file will contain:

* Custom user model
* Profile model

### `accounts/forms.py`

This file will contain:

* Registration form
* Login form
* Profile edit form

### `accounts/views.py`

This file will contain:

* Register view
* Login view
* Logout view
* Profile view
* Edit profile view

### `accounts/urls.py`

This file will contain all URLs related to accounts.

Example pages:

```txt
/accounts/register/
/accounts/login/
/accounts/logout/
/accounts/profile/
/accounts/profile/edit/
```

---

# 5. Books App

The `books` app should be built after the accounts app.

Once users can create accounts and log in, they should be able to add and manage their books.

---

## Step 3 — Create the Books App

### Command

```bash
python manage.py startapp books
```

---

## Books App Structure

```txt
books/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── books/
        ├── add_book.html
        ├── my_books.html
        ├── book_detail.html
        └── search_books.html
```

---

## Books Features to Build

### Book Management

* Add book
* Edit book
* Delete book
* My books page
* Book detail page
* Search books page

### Book Information

Each book can contain:

* Title
* Author
* Description
* Cover image
* Condition
* Availability
* Owner
* Creation date

---

## Important Files

### `books/models.py`

This file will contain:

* Book model
* Book metadata model

### `books/forms.py`

This file will contain:

* Add book form
* Edit book form
* Search form

### `books/views.py`

This file will contain:

* Add book view
* Edit book view
* Delete book view
* My books view
* Book detail view
* Search books view

### `books/urls.py`

This file will contain all URLs related to books.

Example pages:

```txt
/books/add/
/books/my-books/
/books/<id>/
/books/<id>/edit/
/books/<id>/delete/
/books/search/
```

---

# 6. Exchanges App

The `exchanges` app should be built after the books app.

Once books exist in the database, users can request to borrow, receive, give, or exchange them.

---

## Step 4 — Create the Exchanges App

### Command

```bash
python manage.py startapp exchanges
```

---

## Exchanges App Structure

```txt
exchanges/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── exchanges/
        ├── requests.html
        ├── request_detail.html
        └── create_request.html
```

---

## Exchanges Features to Build

### Request System

* Create request
* View sent requests
* View received requests
* Accept request
* Reject request
* Complete request

### Request Status

An exchange request can have several statuses:

| Status      | Meaning                                        |
| ----------- | ---------------------------------------------- |
| `pending`   | The request has been sent but not answered yet |
| `accepted`  | The owner accepted the request                 |
| `rejected`  | The owner rejected the request                 |
| `completed` | The exchange is finished                       |
| `cancelled` | The request was cancelled                      |

---

## Important Files

### `exchanges/models.py`

This file will contain:

* Exchange request model
* Request status
* Relationship between requester, owner, and book

### `exchanges/forms.py`

This file will contain:

* Create request form

### `exchanges/views.py`

This file will contain:

* Create request view
* Sent requests view
* Received requests view
* Request detail view
* Accept request view
* Reject request view
* Complete request view

### `exchanges/urls.py`

This file will contain all URLs related to exchanges.

Example pages:

```txt
/exchanges/
/exchanges/sent/
/exchanges/received/
/exchanges/create/<book_id>/
/exchanges/<id>/
/exchanges/<id>/accept/
/exchanges/<id>/reject/
/exchanges/<id>/complete/
```

---

# 7. Messaging App

The `messaging` app should be built after the exchange system.

Once users can send requests, they need a way to communicate.

---

## Step 5 — Create the Messaging App

### Command

```bash
python manage.py startapp messaging
```

---

## Messaging App Structure

```txt
messaging/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── messaging/
        ├── inbox.html
        └── conversation.html
```

---

## Messaging Features to Build

### Conversations

* Inbox
* Conversation page
* Send message

### Message Information

Each message can contain:

* Sender
* Receiver
* Conversation
* Message content
* Sent date
* Read status

---

## Important Files

### `messaging/models.py`

This file will contain:

* Conversation model
* Message model

### `messaging/forms.py`

This file will contain:

* Message form

### `messaging/views.py`

This file will contain:

* Inbox view
* Conversation view
* Send message view

### `messaging/urls.py`

This file will contain all URLs related to messaging.

Example pages:

```txt
/messages/
/messages/conversation/<id>/
/messages/conversation/<id>/send/
```

---

# 8. Events App

The `events` app should be built after the core book exchange system works.

This app adds community features around books and local events.

---

## Step 6 — Create the Events App

### Command

```bash
python manage.py startapp events
```

---

## Events App Structure

```txt
events/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
└── templates/
    └── events/
        ├── event_list.html
        ├── event_detail.html
        └── create_event.html
```

---

## Events Features to Build

### Event Management

* Event list
* Event detail
* Create event
* Join event
* Share event template

### Event Information

Each event can contain:

* Title
* Description
* Location
* Date
* Time
* Creator
* Participants
* Maximum number of participants
* Event image

---

## Important Files

### `events/models.py`

This file will contain:

* Event model
* Event participants

### `events/forms.py`

This file will contain:

* Create event form

### `events/views.py`

This file will contain:

* Event list view
* Event detail view
* Create event view
* Join event view
* Share event view

### `events/urls.py`

This file will contain all URLs related to events.

Example pages:

```txt
/events/
/events/<id>/
/events/create/
/events/<id>/join/
/events/<id>/share/
```

---

# 9. Core App

The `core` app contains shared pages and global templates.

It should not contain complex business logic.

---

## Core App Structure

```txt
core/
├── views.py
├── urls.py
└── templates/
    └── core/
        ├── home.html
        └── base.html
```

---

## Core Features to Build

* Homepage
* Base template
* Shared layout
* Navigation bar
* Footer
* Common pages

---

## Important Files

### `core/templates/core/base.html`

This file should contain the main HTML structure used by all pages.

It can include:

* HTML head
* CSS links
* Navigation bar
* Main content block
* Footer
* JavaScript links

### `core/templates/core/home.html`

This file should contain the homepage of Livract.

---

# 10. Recommended Build Order

The project should be built in this order:

| Step | App                | Reason                                      |
| ---- | ------------------ | ------------------------------------------- |
| 1    | Project setup      | Required before everything else             |
| 2    | `accounts`         | Users are needed for all main features      |
| 3    | `books`            | Users need to add and manage books          |
| 4    | `exchanges`        | Exchanges depend on books and users         |
| 5    | `messaging`        | Messaging depends on users and requests     |
| 6    | `events`           | Events are extra community features         |
| 7    | Styling and polish | Improve user experience after features work |

---

# 11. Summary of Commands

```bash
django-admin startproject livract
cd livract

python manage.py startapp accounts
python manage.py startapp books
python manage.py startapp exchanges
python manage.py startapp messaging
python manage.py startapp events
python manage.py startapp core

python manage.py runserver
```

---

# 12. Final App Responsibilities

## `accounts`

Handles:

* Users
* Authentication
* Profiles
* Login
* Register
* Logout

---

## `books`

Handles:

* Book creation
* Book editing
* Book deletion
* Book details
* Book search
* User book library

---

## `exchanges`

Handles:

* Borrow requests
* Give requests
* Exchange requests
* Request status
* Request history

---

## `messaging`

Handles:

* Inbox
* Conversations
* Messages between users

---

## `events`

Handles:

* Community events
* Event creation
* Event participation
* Social media share template

---

## `core`

Handles:

* Homepage
* Base template
* Shared layout
* Static pages

---

# 13. Conclusion

This structure keeps Livract clean and scalable.

Each Django app has one specific role, which makes the project easier to develop, debug, and maintain.

The recommended approach is to build the project step by step:

1. Set up the Django project
2. Build user accounts
3. Build book management
4. Build exchange requests
5. Build messaging
6. Build events
7. Improve the interface and user experience
