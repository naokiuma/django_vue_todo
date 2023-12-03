const App = {
    data() {
        return {
            tasks: ['test'],
        }
    },
    compilerOptions: {
        delimiters: ['[[', ']]'],//djangoで{{}}を使っているので、デリミタで別の記述に変える
    },
    methods: {
    },
    created() {
		console.log('start');
    },
}

Vue.createApp(App).mount('#app')