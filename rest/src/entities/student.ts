
// Database level
class Student {
	private _id: number;
	private _username: string;
	private _email: string;
	private _password: string;
	private _age: number;

	constructor(id: number, username: string, email: string, password: string, age: number) {
		this._id = id;
		this._username = username;
		this._email = email;
		this._password = password;
		this._age = age;
	}

	get id(): number {
		return this._id;
	}

	get username(): string {
		return this._username;
	}

	get email(): string {
		return this._email;
	}

	get password(): string {
		return this._password;
	}

	get age(): number {
		return this._age;
	}
}

// For post requests with auto incrementing ids
class NewStudent {
	private username: string;
	private email: string;
	private password: string;
	private age: number;

	constructor(username: string, email: string, password: string, age: number) {
		this.username = username;
		this.email = email;
		this.password = password;
		this.age = age;
	}
}

// For response with relevant values
class StudentResponse {
	private username: string
	private email: string
	private age: number

	constructor(student: Student) {
		this.username = student.username;
		this.email = student.email;
		this.age = student.age;
	}
}



export {
	Student,
	NewStudent,
	StudentResponse
}


