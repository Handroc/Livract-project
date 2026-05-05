# Livract — MVP & Stage 1 Report Draft

| Field | Details |
|---|---|
| **MVP name** | Livract |
| **Type of application** | Mobile application |
| **Main purpose** | Livract is a mobile app that helps casual readers and book clubs in one city **discover books, lend books, give books, exchange books, and communicate around local book sharing**. |

## Target Users

- Casual readers
- Book clubs
- Local reading communities

## Core MVP Features

1. **User accounts and profiles**
2. **Book listing and discovery system**
3. **Borrowing/exchange request system with basic messaging**

This matches the idea of an MVP because it keeps only the core features needed to test the product with early users and gather feedback. Atlassian defines an MVP as the most basic version with only the core features needed to satisfy early adopters and validate the idea.

# Stage 1 Report Draft

## 1. Introduction

This report presents the Stage 1 development process for **Livract**, a mobile application MVP focused on local book sharing. The goal of this stage was to form the team, explore possible project ideas, evaluate their feasibility, select the most relevant MVP concept, and define the project scope, risks, and objectives.

The selected MVP aims to solve the lack of a centralized and easy-to-use platform for sharing, discovering, and discussing books within a local community.

## 2. Team Formation Overview

The team is composed of two members:

| Team member | Responsibilities |
|---|---|
| Andric Assani | Fullstack Developer, UI/UX Designer, QA Tester |
| Lucas Lupon | Fullstack Developer, UI/UX Designer, QA Tester |

The team will use **GitHub** for version control and repository management. **Discord** will be used for regular communication, messages, and weekly meetings. The team plans to communicate twice per week to review progress, identify blockers, and agree on next steps.

Decisions will be made through discussion and agreement. This supports collaboration because effective teams usually rely on clear communication, shared roles, trust, and common goals.

## 3. Brainstorming Process

The team explored ideas related to books, reading communities, and local sharing. The brainstorming process focused on real-world problems, especially the lack of simple tools for people who want to access books without always buying them.

The team considered this direction:

- A community-based book sharing app

## 4. Idea Explored

### Idea 1: Livract — Book Sharing App

**Description:**  
Livract is a mobile app that allows users to list books, search for available books, and request to borrow, receive, or exchange books with other users.

**Problem solved:**  
People do not have a centralized and easy-to-use way to share books, discover available books nearby, or communicate with other readers.

**Target users:**  
Casual readers, book clubs, and local reading communities.

**Main features:**

- User accounts and profiles
- Add and manage book listings
- Search and filter available books
- Send borrowing, giving, or exchange requests
- Accept or reject requests
- Basic messaging
- Book availability status

**Decision:**  
Kept because it is useful, feasible, original, and matches the team’s skills. It also has strong potential to grow into a larger community platform.

## 5. Idea Evaluation

| Criteria | Livract book sharing app |
|---|---:|
| Feasibility | 5/5 |
| Impact | 4/5 |
| Technical alignment | 2.5/5 |
| Innovation | 4/5 |
| Scalability | 5/5 |
| Risk level | 2/5 |

**Conclusion:**  
Livract was selected because it offers the best balance between usefulness, originality, scalability, and feasibility. Even though the technical alignment score is lower because some parts are new to the team, the project remains realistic if the MVP is kept focused.

## 6. Selected MVP Concept

**Livract** is a mobile application that centralizes book sharing in one city. Users can create profiles, list books they own, search for books from other users, and send requests to borrow, receive, or exchange books.

The MVP focuses on a local community first instead of launching everywhere. This makes testing easier and reduces complexity.

**Problem**

People who want to read or share books often lack a simple local platform where they can find available books, contact owners, and organize book exchanges.

**Solution**

Livract provides a mobile platform where users can:

- Create a profile
- Add book listings
- Search and filter books
- Request to borrow, receive, or exchange a book
- Communicate through basic messages
- Track whether a book is available, reserved, unavailable, or exchanged

**Target audience**

The first target users are casual readers and book clubs in one city.

## 7. Reasons for Selection

Livract was selected for the following reasons:

| Reason | Explanation |
|---|---|
| Feasibility | The app can be built with React Native, Node.js, PostgreSQL, Firebase Auth, Figma, and GitHub. |
| Impact | It solves an accessibility problem by helping users access books through local sharing instead of only buying them. |
| Innovation | It combines book discovery, sharing, exchange, and community interaction in one app. |
| Scalability | The app can later expand to more cities, reviews, ratings, events, recommendations, and advanced community features. |
| Team alignment | The project allows both members to work on frontend, backend, database, documentation, design, testing, and GitHub. |
| Controlled risk | The MVP avoids complex features such as online payment, AI recommendations, and web version development. |

## 8. SMART Goals

SMART goals should be specific, measurable, achievable, relevant, and time-bound, which makes progress easier to track and reduces vague objectives.

### Goal 1: Book Listing and Search System

By week 6, the team will develop and test a book listing and discovery system that allows users to add, edit, and view book listings with at least these fields: photo, title, author, condition, and availability. Success will be measured if both team members can create at least 10 sample book listings and successfully search/filter them inside the mobile app.

### Goal 2: Request and Response System

By week 7, the team will implement a borrowing, giving, or exchange request system that allows one user to send a request and another user to accept or reject it. Success will be measured if the team can complete at least 5 full test request flows in the app without critical errors.

### Goal 3: Basic User Testing

By week 9, the team will conduct MVP testing with at least 5 test users and collect feedback on usability, core features, and problems encountered. Success will be measured if the team receives written feedback from all 5 users and identifies at least 3 improvements to apply in the next development stage.

## 9. Project Scope

Project planning should clarify the “what,” “how,” and “when” of the project, including project scope, risks, milestones, and deliverables.

### In Scope

- Mobile app MVP
- User registration and authentication
- User profiles
- Add and manage book listings
- Events
- Review / Ratings
- Book listing fields:
  - Photo
  - Title
  - Author
  - Condition
  - Availability
- Search and filter books
- Borrowing, giving, or exchange request system
- Accept/reject requests
- Basic messaging between users
- Book availability status
- **Exchange status tracking** instead of full delivery tracking

### Out of Scope

- Online payment
- AI recommendation system
- Web version
- Advanced delivery/shipping logistics

## 10. Risks and Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Database complexity | The database may become difficult to design because the app needs users, books, requests, messages, and availability statuses. | Start with a simple database structure and test it early before adding extra features. |
| Communication issues | Misunderstandings could slow progress or cause duplicated work. | Use Discord for regular updates, meet twice per week, and track tasks through GitHub. |
| Users may not trust strangers | Users may hesitate to lend, give, or exchange books with unknown people. | Add user profiles, basic messaging, availability status, and accept/reject requests to make exchanges more transparent. |
| Scope creep | The team may try to add too many features, such as events, ratings, or recommendations. | Keep these features out of scope and focus only on the MVP features. |
| Technical learning curve | React Native, PostgreSQL, backend logic, and authentication may require learning time. | Assign features clearly, build small prototypes, and test each part progressively. |

## 11. Conclusion

Livract is a strong MVP choice because it solves a clear local accessibility problem around books. Instead of creating a simple review app or a limited event app, Livract focuses on the most useful core need: allowing readers to list, discover, request, and exchange books.

The project is feasible because the team has selected realistic technologies and a limited feature set. The MVP avoids complex features such as online payment, AI recommendations, reviews, ratings, and web development. Future versions could expand with book events, reviews, ratings, recommendations, and support for multiple cities.
