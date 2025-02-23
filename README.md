### **Gas Utility Service Management System**

The **Gas Utility Service Management System** is a web-based application designed to streamline the process of managing service requests for gas utility companies. It allows users to submit service requests, track their status, and enables support staff to manage and resolve these requests efficiently. Built with Django, this system provides a robust and scalable solution for handling gas utility services.

---

## **Features**

### **User Features**
1. **User Authentication**:
   - Users can sign up, log in, and manage their accounts.
   - Passwords are securely hashed for enhanced security.

2. **Service Request Submission**:
   - Users can submit service requests for issues such as gas leaks, meter reading discrepancies, or billing problems.
   - Users can attach files (e.g., images or documents) to provide additional context for their requests.

3. **Request Tracking**:
   - Users can view the status of their submitted requests (Pending, In Progress, Resolved).
   - Users receive updates on the resolution of their requests.

4. **Profile Management**:
   - Users can update their profile information and view their request history.

---

### **Support Staff Features**
1. **Request Management**:
   - Support staff can view all submitted service requests.
   - Staff can update the status of requests (e.g., mark as In Progress or Resolved).
   - Staff can add remarks and track actions taken on each request.

2. **Role-Based Access**:
   - Support staff have elevated permissions to manage requests and view user details.
   - Regular users can only submit and track their own requests.

3. **Action Tracking**:
   - Staff can log actions taken on each request, along with timestamps for better accountability.

---

### **Admin Features**
1. **Dashboard**:
   - Admins have access to a comprehensive dashboard to monitor all requests, users, and support staff activities.

2. **User Management**:
   - Admins can create, update, or delete user accounts.
   - Admins can assign or revoke support staff roles.

3. **Analytics**:
   - Admins can view reports and analytics on request resolution times, user activity, and more.

---

## **Technologies Used**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default), PostgreSQL (production-ready)
- **Authentication**: Django's built-in authentication system
- **File Storage**: Django's `FileField` for handling file uploads
- **Version Control**: Git

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or higher
- Pip (Python package manager)
- Git (optional)

### **Installation Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anujyadav007/gas-utility.git
   cd gas-utility

  python -m venv venv
 source venv/bin/activate  

 pip install -r requirements.txt

 python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Access the Application:

Open your browser and go to http://127.0.0.1:8000/.
Use the superuser credentials to log in as an admin.




### Screenshots

https://drive.google.com/drive/folders/15NfzY8k6fG4JZJCj8Py4hSGkSiUDUc-j?usp=sharing



