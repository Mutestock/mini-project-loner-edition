import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar/';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule }  from '@angular/material/button'
import { MatTabsModule } from '@angular/material/tabs';
import { TeachersComponent } from './teachers/teachers.component';
import { StudentsComponent } from './students/students.component';
import { GradesComponent } from './grades/grades.component'

@NgModule({
  declarations: [
    AppComponent,
    TeachersComponent,
    StudentsComponent,
    GradesComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatTabsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {  }
