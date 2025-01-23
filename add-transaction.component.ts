// src/app/components/add-transaction/add-transaction.component.ts

import { Component } from '@angular/core';
import { ApiService } from '../../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-transaction',
  templateUrl: './add-transaction.component.html',
  styleUrls: ['./add-transaction.component.css'],
})
export class AddTransactionComponent {
  description: string = '';
  amount: number = 0;
  type: string = 'expense'; // Can be either 'expense' or 'income'
  errorMessage: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onAddTransaction(): void {
    const newTransaction = {
      description: this.description,
      amount: this.amount,
      type: this.type,
    };

    this.apiService.addTransaction(newTransaction).subscribe(
      (response) => {
        this.router.navigate(['/dashboard']);
      },
      (error) => {
        this.errorMessage = 'Failed to add transaction. Please try again.';
      }
    );
  }
}
