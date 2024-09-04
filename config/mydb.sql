CREATE DATABASE mydb;
USE mydb;


CREATE TABLE positions(
    id_position INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(250) NULL,
    description TEXT NULL,
    salary DOUBLE NOT NULL DEFAULT 0.00,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    created_by INT,
    updated_by INT,
    deleted_by INT,
    PRIMARY KEY (id_position)
);
ALTER TABLE positions ADD FOREIGN KEY (created_by) REFERENCES employees(id_employee);
ALTER TABLE positions ADD FOREIGN KEY (updated_by) REFERENCES employees(id_employee);
ALTER TABLE positions ADD FOREIGN KEY (deleted_by) REFERENCES employees(id_employee);

CREATE TABLE employees(
    id_employee INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    lastname VARCHAR(45) NOT NULL,
    addmission_date DATE NOT NULL,
    email VARCHAR(45) NOT NULL,
    position_id INT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    created_by INT,
    updated_by INT,
    deleted_by INT,
    PRIMARY KEY (id_employee)
);
ALTER TABLE employees ADD FOREIGN KEY (created_by) REFERENCES employees(id_employee);
ALTER TABLE employees ADD FOREIGN KEY (updated_by) REFERENCES employees(id_employee);
ALTER TABLE employees ADD FOREIGN KEY (deleted_by) REFERENCES employees(id_employee);
ALTER TABLE employees ADD FOREIGN KEY (position_id) REFERENCES positions(id_position);

CREATE TABLE users(
    id_user INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(45) NOT NULL,
    userpassword VARCHAR(45) NOT NULL,
    employee_id INT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    created_by INT,
    updated_by INT,
    deleted_by INT,
    PRIMARY KEY (id_user)
);
ALTER TABLE users ADD FOREIGN KEY (created_by) REFERENCES employees(id_employee);
ALTER TABLE users ADD FOREIGN KEY (updated_by) REFERENCES employees(id_employee);
ALTER TABLE users ADD FOREIGN KEY (deleted_by) REFERENCES employees(id_employee);
ALTER TABLE users ADD FOREIGN KEY (employee_id) REFERENCES employees(id_employee);