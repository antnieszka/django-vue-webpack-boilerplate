<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png">
    <br>
    <img class="logo" src="./assets/dj.png">
    <hello/>
    <p>Welcome to your Django - Vue.js app</p>
  </div>
</template>

<script>
import Hello from "./components/Hello";

export default {
  name: "app",
  components: {
    Hello
  }
};
</script>

<style>
html {
  height: 100%;
}

body {
  height: 100%;
}

#app {
  color: #2c3e50;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px;
}
</style>
