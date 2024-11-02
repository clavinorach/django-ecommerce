# Django eCommerce Project - Clavstore

This project is an eCommerce platform that I built using Django for the backend. The platform integrates several third-party services, such as Monday.com for automating user registration data. The app provides functionalities for managing products, customer accounts, shopping carts, and order processing.
This project also includes deployment on Heroku, utilizing PostgreSQL as the database in production, along with AWS integration that is ready to use (but not currently active) for hosting media and other services.

## Project Covered:

- Building an eCommerce Store with Django: Fundamentals of Django and set up the foundation for an eCommerce website.
- Payment Integration with PayPal: Implement payment processing using API PayPal integration.
- Shopping Cart Development: Create a shopping cart feature for this eCommerce site.
- User Management: Implement user management functionality, including login, logout, and registration.
- Email Verification: Add email verification features to enhance user management.
- AWS Integration: AWS is configured for integration, including Amazon S3, Amazon RDS, and Amazon Elastic Beanstalk, but currently, it is not in use.
- Shipping and Order Functionality: Implement shipping and order processing features.
- Styling and Validation: Enhance the user interface and ensure data validation.
- Password Management: Implement secure password management features.
- Cart Functionality: Handle shopping cart functionality, including sessions, adding, deleting, updating, testing, and optimization.

## Features

- User Registration and Authentication (login, logout, register).
- Product Management (list products, categories, manage stock).
- Shopping Cart and Checkout with payment integration.
- Admin Dashboard for managing orders, users, and products.
- Third-Party Integrations:
  - Monday.com integration for automating data related to user registration.
  - Amazon S3 (optional, not currently in use) for media file storage.
- Responsive Design for an optimized experience on both desktop and mobile devices.

## Technology Stack

This eCommerce project utilizes the following technologies and frameworks:

- **Programming Language**: Python (v3.10+)
- **Framework**: Django (v4.x)
- **Database**: PostgreSQL (Heroku production & Local development)
- **Deployment Platform**: Heroku
- **Authentication**: Custom user authentication with Django's built-in capabilities
- **Payment Integration**: PayPal 
- **Automation Integration**: Monday.com for automating user registration data
- **Version Control**: Git, GitHub
- **AWS Integration**: Amazon S3 (ready but not currently in use)

## Installation Guide

### Prerequisites
- **Python 3.10+**: Ensure Python is installed and available on your system.
- **PostgreSQL**: A PostgreSQL database for production use.
- **Heroku CLI**: Used for deploying the application.
- **Git**: Version control system.

### Setting Up the Project Locally

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/django-ecommerce.git
   cd django-ecommerce
   ```

2. **Create a Virtual Environment and Activate It**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Project Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create and Configure `.env` File**
   - Create a `.env` file in the root of your project with the following variables:
   ```
   # Local database configuration
   DB_NAME=django_ecommerce
   DB_USER=your_postgres_user
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432

   # Email configuration settings:
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   DATABASE_URL=postgres://localhost:5432/your_database_name
   SSL_REQUIRE=False

   # Monday.com API key and board ID
   MONDAY_API_KEY=your_monday_api_key
   MONDAY_BOARD_ID=your_board_id
   
   AWS_ACCESS_KEY_ID=your_aws_key (optional)
   AWS_SECRET_ACCESS_KEY=your_aws_secret (optional)
   ```

5. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser Account**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser to access the application.


## Running Tests

1. **Run All Tests**
   ```sh
   python manage.py test
   ```
## How to Test PayPal Payment

Please be sure to check out the following links:

- **PayPal Links**:
  - [Create a PayPal account](https://www.paypal.com/signup)
  - [Create a Sandbox account](https://developer.paypal.com/docs/api-basics/sandbox/accounts/) - You must first have a PayPal account to log in and create your Sandbox accounts.
  - [Login to your Sandbox accounts](https://www.sandbox.paypal.com/)
  - [PayPal API and documentation](https://developer.paypal.com/docs/api/overview/) (Useful as a general reference ONLY)
  - [Customize the PayPal buttons](https://developer.paypal.com/docs/checkout/how-to/customize-button/)
  - [Validate user input](https://developer.paypal.com/docs/checkout/integration-features/validation/)

For Sandbox mode:

- **Test credit card details**:
  - **Dummy card**: `4032032685528157`
  - **Dummy phone number**: `203-555-0134`

## Additional Notes
- **AWS Integration**: The app is pre-configured for AWS services (Amazon S3, Amazon RDS), but those features are currently turned off. You can enable them by providing the necessary credentials in your `.env` file.
- **Static Files**: During deployment, `DISABLE_COLLECTSTATIC=1` can be used to disable static file collection if necessary.

## Contact
If you have any questions or issues, feel free to reach out:
- **GitHub**: [Clavino Ourizqi Rachmadi](https://github.com/clavinorach)
- **LinkedIn**: [Clavino Ourizqi Rachmadi](https://www.linkedin.com/in/clavinorachmadi/)
