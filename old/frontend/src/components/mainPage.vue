<template>
  <div class="mainPage">
    <h1>{{ msg }}</h1>
    <h2>h2 main page</h2>
    <prefNavigation></prefNavigation>

    <ul>
      <li v-for="planet in jsonInput">
        <button
          type="button"
          class="btn"
          @click="showModal">
          {{ planet.title }}
        </button>
      </li>
    </ul>
    <input type="checkbox" id="checkbox" v-model="show1">
    <label for="checkbox">component 1</label>
    <input type="checkbox" id="checkbox" v-model="show2">
    <label for="checkbox">component 2</label>
    <input type="checkbox" id="checkbox" v-model="show3">
    <label for="checkbox">component 3</label>
    <contentbox v-bind:class="{'is-shown' : !show1 }"><p slot="body">
      <ul>
        <li v-for="item in firstComponentData">
          {{ item }}
        </li>
      </ul>
    </p></contentbox>
    <contentbox v-bind:class="{'is-shown' : !show2 }"><p slot="body">
      <ul>
        <li v-for="item in secondComponentData">
          {{ item }}
        </li>
      </ul>
    </p></contentbox>
    <contentbox v-bind:class="{'is-shown' : !show3 }"><p slot="body">
      <ul>
        <li v-for="item in thirdComponentData">
          {{ item }}
        </li>
      </ul>
    </p></contentbox>
    </ul>

    <modal
      v-show="isModalVisible"
      @close="closeModal"
    />







  </div>
</template>

<script>
import contentbox from './contentbox'
import prefNavigation from './prefNavigation'
import {jsonInput} from '../dataJSON'

export default {
  name: 'mainPage',
  data () {
    return {
      msg: "mainPage message",
      jsonInput,
      isModalVisible: false,
      list: {"1":"ich","2":"du","3":"er"},
      firstComponentData: undefined,
      secondComponentData: undefined,
      thirdComponentData: undefined,
      show1: true,
      show2: true,
      show3: true,
    }
  },
  components: {
    contentbox,
    prefNavigation
  },
  methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
      getLists() {
        fetch("http://localhost:5000/")
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data);
          this.list = data;
        })
      },
      getFirstComponentData() {
        fetch("http://localhost:5000/firstComponent")
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data);
          this.firstComponentData = data;
        })
      },
      getSecondComponentData() {
        fetch("http://localhost:5000/secondComponent")
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data);
          this.secondComponentData = data;
        })
      },
      getThirdComponentData() {
        fetch("http://localhost:5000/thirdComponent")
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data);
          this.thirdComponentData = data;
        })
      },
    },
    beforeMount(){
      this.getFirstComponentData();
      this.getSecondComponentData();
      this.getThirdComponentData();
    }
  };

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .is-shown {
    display: none;
  }
  #mainPage {
    float: left;
  }
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
