# Weather Application

A Django-based weather application that provides weather information and forecasts. The application is containerized using Docker and can be deployed on AWS EC2 or ECS Fargate.

## Project Structure

```
weather-app/
├── weather/                      
│   ├── migrations/            
│   │   └── __init__.py
│   ├── static/                  
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/            
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── weather_project/            
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── nginx/                   
│   ├── Dockerfile
│   ├── nginx.conf        
│   ├── app.conf              
│   └── error_pages/       
│       ├── 404.html
│       └── 50x.html
│
├── static/                   
├── media/                  
├── logs/                       
│
├── docker-compose.ec2.yml     
├── docker-compose.fargate.yml
├── Dockerfile                  
├── requirements.txt           
├── .env                        
└── .dockerignore            
```

## Technology Stack

- **Backend**: Django 5.0
- **Database**: PostgreSQL (AWS RDS)
- **Web Server**: Nginx
- **Containerization**: Docker
- **Deployment**: AWS EC2/ECS Fargate
- **Frontend**: Bootstrap 5, HTML, CSS, JavaScript
- **Authentication**: Django Authentication System
- **Weather Data**: OpenWeather API

## Setup and Deployment

### Prerequisites

- Docker and Docker Compose
- AWS Account (for RDS and deployment)
- Python 3.11+
- PostgreSQL client (for local development)

### Environment Variables

Create a `.env` file with the following variables:

```env
# Django settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database settings (AWS RDS)
DB_NAME=weather-app-db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=your-rds-endpoint
DB_PORT=5432
DB_SSL=True

# OpenWeather API
OPENWEATHER_API_KEY=your-api-key
```

### Local Development

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Docker Deployment

#### EC2 Deployment (with Nginx)

1. Build and start the containers:
   ```bash
   docker compose -f docker-compose.ec2.yml up -d
   ```

2. Run migrations:
   ```bash
   docker compose -f docker-compose.ec2.yml exec web python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   docker compose -f docker-compose.ec2.yml exec web python manage.py createsuperuser
   ```

#### ECS Fargate Deployment

1. Build and start the containers:
   ```bash
   docker compose -f docker-compose.fargate.yml up -d
   ```

2. Run migrations:
   ```bash
   docker compose -f docker-compose.fargate.yml exec web python manage.py migrate
   ```

## Features

- User authentication (login, registration, profile management)
- Weather information display
- Responsive design
- Custom error pages
- Health check endpoint
- Secure configuration
- Docker containerization
- Nginx reverse proxy
- AWS RDS integration

## Security Considerations

- SSL/TLS encryption for database connections
- Secure headers in Nginx configuration
- Environment variable management
- Django security settings
- Docker security best practices

## Monitoring and Maintenance

- Health check endpoints
- Logging configuration
- Error tracking
- Database backups
- Container health checks

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
