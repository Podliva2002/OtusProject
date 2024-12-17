import { defineStore } from "pinia";

export const userRental = defineStore("rental", {
    state: () => ({
        rentals: localStorage.getItem("rental") || 'Прокат сноубордов',
        listRentals: [
            'Прокат сноубордов',
            'Прокат тюбингов',
            'Прокат велосипедов'
        ],
    }),
    actions: {
        async changeRental (rent) {
            localStorage.setItem("rental", rent);
            this.rentals = rent;
        }
    }
});