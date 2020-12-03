(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const state_output = document.querySelector('#state');
    async function poll(task_id){
        const res = await fetch('http://localhost:8000/api/' + task_id.toString() + '/status', {
            method: 'GET',
        });
        const json = await res.json();
        let state = state_output.innerText = json?.state;
        return state;
    }

    const btn = document.querySelector('#test-btn'); 
    const output = document.querySelector('#output');
    btn.addEventListener('click', async (event) => {
        event.preventDefault();
        output.innerText = '';
        state_output.innerText = '';

        // tells server to start a long running task
        const res = await fetch('http://localhost:8000/api/random', {
            method: 'GET',
        });
        let task_id = (await res.json())?.task_id;
        output.innerText = task_id;
        const timer = setInterval(async function(){
            // polls the server
            let state = await poll(task_id);
            output.innerText = task_id;
            console.log(state);
            if (state === 'SUCCESS') {
                clearInterval(timer);
            }
        }, 2000);
        
    });

})();