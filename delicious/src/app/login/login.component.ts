import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service'; // Substitua pelo caminho correto
import { Router } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  myform: FormGroup;
  errorMessage: string | undefined;
  
  constructor(private authService: AuthService, private router: Router){
    this.myform = new FormGroup({
      username: new FormControl(''),
      password: new FormControl('')
    })
  }

  ngOnInit(): void{
    this.myform = new FormGroup({
      username: new FormControl(''),
      password: new FormControl('')
    })
  }

  get f(){
    return this.myform.controls;
  }

  onSubmit() {
    this.authService.login(this.f['username'].value, this.f['password'].value)
      .pipe(first())
      .subscribe(
        data => {
          console.log(data);
          this.router.navigate(['/home']);
        },
        error => {
          console.error('Erro de autenticação:', error);
          this.errorMessage = "UserName or Password not valid";
        }
      );
  }


}