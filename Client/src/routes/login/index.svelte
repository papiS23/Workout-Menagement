<!-- TODO
    - uzupełnic paramety inputa;
    - napisac requesty;
    - stworzyć panel do resetu hasła;
    - połączyć buttona logowania z przejściem do strony głównej ( request - jesli przejdzie przez logowanie to przepuść na strone glowna) 
 -->

<script lang="ts">
    import Icon from 'mdi-svelte';
    import { mdiFacebook, mdiFormTextboxPassword } from '@mdi/js';
    import { mdiGoogle } from '@mdi/js';
    import { mdiTwitter } from '@mdi/js';
    import { mdiEmailPlusOutline } from '@mdi/js';
    let login = "";
    console.log(login);
    let password = "";

    const getData: svelte.JSX.FormEventHandler<HTMLFormElement> = (event) =>{
        event.preventDefault();
        
        var login_data = {
            login: login,
            password: password
        }

        login = '';
        password = '';

        console.log(login_data);
    }
</script>

<div class="container">
    
    <nav class="navigation">
        <button class="navigation__buttons"><Icon path={mdiFacebook} color="black" size="1.5em" /></button>
        <button class="navigation__buttons"><Icon path={mdiGoogle} color="black" size="1.5em"/></button>
        <button class="navigation__buttons"><Icon path={mdiTwitter} color="black" size="1.5em"/></button>
        <button class="navigation__buttons"><Icon path={mdiEmailPlusOutline } color="black" size="1.5em"/></button>
    </nav>
    <div class="line">
        <div class="line__prev"></div>
        <p class="line__text">or</p>
        <div class="line__next"></div>
    </div>
    <form class="form" on:submit={getData}>
        <!-- uzupełnic inputy o parametry -->
        <label class="form__label">Email
            <input class="form__label--input" type="email" bind:value={login}>
        </label>
        <label class="form__label">Password
            <input class="form__label--input" type="password"  bind:value={password}>
        </label>
        <button type="submit" class="form__button">Login</button>
    </form>
    <footer class="footer">
        <p class="footer__text">Did you forgot your password?</p>
        <a class="footer__link" href="/register">Reset Password</a>
    </footer>
</div>

<style lang="scss" scoped>
    

    .navigation{
        width: 100%;
        margin: 10% 0;
        padding: 1% 10%;
        display: flex;
        justify-content: space-between;

        &__buttons{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 3%;
            outline: none;
            border: none;
            border-radius: 20%;
        }
    }

    .line{
        width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;

        &__prev, &__next{
            width: 25%;
            height: 2px;
            background-color: black;
        }
    }

    .form{
        width: 100%;
        height: 40vh;
        padding: 0 10%;
        display: flex;
        justify-content: space-around;
        flex-direction: column;

        &__label{
            width: 100%;
            display: flex;
            flex-direction: column;

            &--input{
                width: 100%;
                padding: 2%;
                border-radius: 7px;
                outline: none;
                border: solid 2px black;

            }
        }

        &__button{
            widows: 100%;
            padding: 5%;
            border: none;
            border-radius: 7px;
        }
    }

    .footer{
            width: 100%;
            padding: 10% 5%;
            display: flex;
            justify-content: space-around;

            &__text, &__link{
                font-size: .8em;
            }
        }
</style>