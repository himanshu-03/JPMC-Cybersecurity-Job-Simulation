# Application Security Fundamentals

## Objective: 

Build a secure Django web application with One-Time Password (OTP) integration.

## Step 1: Environment Setup

### Install Python

Ensure Python3 is installed on your machine. Open a terminal and type:

```bash
python3 --version
```

You should see the Python version displayed. If not, download and install Python from python.org.

### Environment Isolation
To keep your project dependencies isolated, you can use one of the following methods:

#### Using Anaconda / Miniconda
1. Install Anaconda or Miniconda from their website.
2. Create and activate a new environment:

```bash
conda create --name forageenv python=3.9
conda activate forageenv
```

#### Using venv
1. Create and activate a virtual environment:

```bash
python3 -m venv forageenv
source forageenv/bin/activate  # On Windows use `forageenv\Scripts\activate`
```

## Step 2: Project Setup

1. Navigate into the project directory:

    ```bash
    cd mysite
    ```

2. Install the required Python modules:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Migrate the database to sync it with the existing configuration:

    ```bash
    python3 manage.py migrate
    ```

4. Create a site admin user:

    ```bash
    python3 manage.py createsuperuser
    ```

    Follow the prompts to enter a username, email, and password.

5. Run the web application:

    ```bash
    python3 manage.py runserver
    ```

## Step 3: Install Django OTP

Follow the Django OTP installation docs at [django-otp-official.readthedocs.io](django-otp-official.readthedocs.io).

1. Install Django OTP:

    ```bash
    pip3 install django-otp
    ```

2. Modify settings.py:

    - Add 'django_otp' to INSTALLED_APPS.
    - Add the otp_totp plugin to INSTALLED_APPS:

    ```python
    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        ...
    ]
3. Configure middleware to include DjangoOTP:

    ```python 
    MIDDLEWARE = [
        ...
        'django_otp.middleware.OTPMiddleware',
        ...
    ]
    ```

3. Apply migrations for Django OTP:

    ```bash
    python3 manage.py migrate
    ```

## Step 4: Modify urls.py

1. Open urls.py and add the following import statement:

    ```python
    from django_otp.admin import OTPAdminSite
    ```

2. Replace the default admin.site class with OTPAdminSite:
    
    ```python
    admin.site.__class__ = OTPAdminSite
    ```

## Step 5: Run the Server and Add a Device

1. Stop the running web server if it's active (Ctrl-C).
2. Restart the web server:
    ```bash
    python3 manage.py runserver
    ```
3. Navigate to http://localhost:8000/admin/.
4. Log in using the admin credentials you created earlier.
5. Add a device and configure OTP:
    - Go to the admin interface.
    - Add a new OTP device.
    - Click on the QR code link and scan it using an OTP app (like Google Authenticator).
    - Copy the QR code link to answer the final quiz question. Replace the `secret` value with `<SECRET>`.

Congratulations! You have successfully set up a Django web application with OTP integration.

## Skills Gained:

1. Web Application Development
2. Two-Factor Authentication (2FA)
3. Secure Coding Practices
4. User Management