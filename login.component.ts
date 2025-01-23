import { Component } from '@angular/core';
import { ApiService } from '../../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onLogin(): void {
    this.apiService.login(this.username, this.password).subscribe(
      (response) => {
        // Assuming the API returns a user object on successful login
        localStorage.setItem('token', response.token); // Save the token in local storage
        this.router.navigate(['/dashboard']);
      },
      (error) => {
        this.errorMessage = 'Login failed. Please check your credentials.';
      }
    );
  }
}