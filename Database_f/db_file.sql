Create database Teams;
Use Teams;

CREATE TABLE Department (
	department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE Member (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  pass_word VARCHAR(20),
  phone_number VARCHAR(20),
  department_id INT,
  FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

ALTER TABLE Member AUTO_INCREMENT = 7000;

CREATE TABLE Team_Lead (
  team_lead_id INT AUTO_INCREMENT PRIMARY KEY, 
  member_id INT,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Super_Admin (
  super_admin_id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Team (
  team_id INT PRIMARY KEY,
  team_name VARCHAR(50)
);

Create Table All_teams (
    index_id INT AUTO_INCREMENT,
	team_id INT,
	member_id INT,
	role VARCHAR(50),
	FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

CREATE TABLE Tasks (
  task_id INT PRIMARY KEY,
  task_name VARCHAR(100),
  task_start_date DATE,
  task_end_date DATE,
  team_id INT,
  member_id INT,
  task_submitted BOOLEAN,
  task_submitted_on_time BOOLEAN,
  FOREIGN KEY (team_id) REFERENCES Team(team_id),
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Leaves(
	request_id INT PRIMARY KEY,
    member_id INT,
	start_date DATE,
    end_date DATE,
	reason VARCHAR(500),
    Approved_request BOOLEAN,
    FOREIGN KEY (member_id) REFERENCES Member(member_id));
    

show tables;    

INSERT INTO Member (name, email, phone_number) 
VALUES 
  ('John Doe', 'john@example.com', '555-1234'),
  ('Jane Doe', 'jane@example.com', '555-2345'),
  ('Bob Smith', 'bob@example.com', '555-3456'),
  ('Sarah Park', 'sarah@example.com', '555-4567'),
  ('Mike Chan', 'mike@example.com', '555-5678'),
  ('Danny', 'danny@example.com', '555-1227'),
  ('Dhin', 'Dhin@example.com', '555-2327'); 
  
INSERT INTO Team_Lead (member_id)
VALUES
  (7000),
  (7001),
  (7003);   
  
INSERT INTO Super_Admin (member_id)
VALUES
  (7000),	
  (7001),
  (7003);  
  
INSERT INTO Team (team_id, team_name)
VALUES
  (1, "A"),
  (2, "B"),
  (3, "C");

INSERT INTO All_teams (team_id, member_id,role)

VALUES
	(1,7000,'CSE'),
    (2,7001,'CSE'),
	(3,7003,'CSE'); 

DROP TABLE All_teams;
Create Table All_teams (
    index_id INT AUTO_INCREMENT PRIMARY KEY,
	team_id INT,
	member_id INT,
	role VARCHAR(50),
	FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);
INSERT INTO All_teams (team_id, member_id,role)

VALUES
	(1,7000,'CSE'),
    (2,7001,'CSE'),
	(3,7003,'CSE');    
    

Select * from Member;
Select * from All_Teams;
Select * from Team;
Select * from Team_Lead;
Select * from Super_admin;  
delete from Member;

SELECT * from All_Teams;
