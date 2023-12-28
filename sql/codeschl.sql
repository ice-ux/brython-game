use codeschl;
-- 用户表
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(100),
    RegistrationDate DATE NOT NULL
);

-- 课程表
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    CourseDescription TEXT,
    CreationDate DATE NOT NULL
);

-- 章节表
CREATE TABLE Chapters (
    ChapterID INT PRIMARY KEY AUTO_INCREMENT,
    ChapterName VARCHAR(100) NOT NULL,
    ChapterContent TEXT,
    CourseID INT,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 学习记录表
CREATE TABLE LearningRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    CourseID INT,
    ChapterID INT,
    LearningStatus ENUM('未完成', '已完成', '在学中'),
    LearningDate DATE NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ChapterID) REFERENCES Chapters(ChapterID) ON DELETE CASCADE ON UPDATE CASCADE
);