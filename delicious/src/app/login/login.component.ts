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
  
  constructor(private authService: AuthService){
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
        },
        error => {
          console.error('Erro de autenticação:', error);
          // Verifique se o erro é relacionado a nome de usuário ou senha incorretos
          if (error && error.status === 400) {
            // Erro 400 geralmente indica credenciais inválidas
            console.log('Nome de usuário ou senha incorretos.');
          } else {
            // Trate outros tipos de erros, se necessário
            console.error('Erro não tratado:', error);
          }
        }
      );
  }



  // username: string;
  // password: string;

  // constructor(private authService: AuthService, private router: Router) {
  //   this.username = '';
  //   this.password = '';
  // }

  // onLogin() {
  //   console.log("username:", this.username);
  //   console.log("password:", this.password);
  //   this.authService.login(this.username, this.password);
  //   console.log("FEITO")
  //   this.router.navigate(['/home']);
  // }
}