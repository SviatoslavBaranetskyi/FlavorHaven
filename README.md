# FlavorHaven
RESTful restaurant service
## Idea
The main idea is to create an API for a restaurant service.
# Technological stack
- Django
- Django Rest Framework
- PostgreSQL
- Swagger
# Description:
- Retrieve list of all dishes<br>
GET /api/v1/menu<br>
- Retrieve details of a dish by ID<br>
GET /api/v1/menu/{id}<br>
- Retrieve list of all categories<br>
GET /api/v1/categories<br>
- Retrieve list of dishes by category ID<br>
GET /api/v1/categories/{category_id}/dishes<br>
- Retrieve list of reservations<br>
GET /api/v1/reservations<br>
- Create a new reservation<br>
POST /api/v1/reservations<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"guests": 10,<br>
&nbsp;&nbsp;&nbsp;"date": "2024-04-11",<br>
&nbsp;&nbsp;&nbsp;"time": "string",<br>
&nbsp;&nbsp;&nbsp;"first_name": "string",<br>
&nbsp;&nbsp;&nbsp;"last_name": "string",<br>
&nbsp;&nbsp;&nbsp;"phone_number": "string",<br>
&nbsp;&nbsp;&nbsp;"special_request": "string"<br>
}
# Future plans:
- Role-based Access Control
- Localization
- Webhooks
## Developer
Sviatoslav Baranetskyi

Email: svyatoslav.baranetskiy738@gmail.com
