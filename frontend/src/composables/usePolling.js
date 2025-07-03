import { ref, onMounted, onUnmounted } from "vue";



const usePolling = (method, timeInterval = 10000) => {

  const interval = ref(null);

  const callMethod = ref(method);

  const isPolling = ref(false);



const clear = () => {

    clearInterval(interval.value);

    interval.value = null;

    isPolling.value = false;

  };



const fetchData = (poll = true) => {

    callMethod.value();

    if (poll) {

      // start interval

      interval.value = setInterval(() => {

        callMethod.value();

      }, timeInterval);

    } else {

      clear();

    }

  };



const start = () => {

    // clear any existing polling calls

    clear();

    // set polling flag to true

    isPolling.value = true;

    // fetch data

    fetchData();

  };



onMounted(() => isPolling.value && fetchData());



onUnmounted(clear);



return {

    start,

    clear,

  };

};



export default usePolling;