import { defineStore } from "pinia";

export const userRental = defineStore("rental", {
    state: () => ({
        rentals: null,
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