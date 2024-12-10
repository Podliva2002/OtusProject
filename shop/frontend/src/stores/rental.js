import { defineStore } from "pinia";

export const userRental = defineStore("rental", {
    state: () => ({
        rentals: 'Прокат сноубордов',
        listRentals: [
            'Прокат сноубордов',
            'Прокат тюбингов',
            'Прокат велосипедов'
        ],
    }),
    actions: {
        changeRental (rent) {
            this.rentals = rent;
        }
    }
});