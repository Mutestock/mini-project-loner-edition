import { Component, OnInit } from '@angular/core';

export interface Student {
  id: number;
  first_name: string;
  last_name: string;
  phone_number: string;
  email: string;
  created_at: Date;
  updated_at: Date;
}



@Component({
  selector: 'app-students',
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.scss']
})
export class StudentsComponent implements OnInit {
  columnsToDisplay: string[] = ['id', 'first_name', 'last_name', 'email']
  dataSource: Student[] = [];


  constructor() { }

  ngOnInit(): void {
  }

}
