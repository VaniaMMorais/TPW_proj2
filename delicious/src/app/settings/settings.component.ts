import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { MyApiService } from '../my-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.css'
})
export class SettingsComponent implements OnInit{

  username: any;
  firstName: any;
  lastName: any;
  email: any;

  constructor(private authService: AuthService, private myApiService: MyApiService, private router: Router) {}

  ngOnInit(): void {
    const currentUser = this.authService.getCurrentUser();
    this.username = currentUser.username;
    this.firstName = currentUser.first_name;
    this.lastName = currentUser.last_name;
    this.email = currentUser.email;
  }

}
