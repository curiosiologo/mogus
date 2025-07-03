/** @type {import('tailwindcss').Config} */


export default {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    extend: {
      dropShadow: {
        '3xl': '0 3px 3px rgb(0, 229, 255)',
        '4xl': [
            '0 3px 3px rgb(255, 0, 0)',
            '0 3px 3px rgb(255, 0, 0)']
  },
  plugins: [],
}
}
}